from flask import (Flask, render_template, current_app, request, url_for, redirect)
import requests
app = Flask(__name__,
            static_url_path='/static', 
            static_folder='static',
            template_folder='templates'
            

            )


@app.route('/')
def index():
    return render_template('index.html')



def get_depenancies(package, version):
    response = requests.get(f"https://registry.npmjs.org/{package}/{version}")
    response_data = response.json()
    dependancies = {}
    if response.status_code == 200:
        if "devDependencies" in response_data.keys():
            dependancies = {**dependancies, **response_data["devDependencies"]}
        if "dependencies" in response_data.keys():
            dependancies = {**dependancies, **response_data["dependencies"]}
    return response.status_code, dependancies



def get_latest_version(package, adj):
    response = requests.get(f"https://registry.npmjs.org/{package}/{adj}")
    response_data = response.json()
    version = ""
    if response.status_code == 200:
        if "version" in response_data.keys():
            version = response_data.get("version")
    return response.status_code, version
    
    
def parse_depth_1_dependancies(dependancies):
    depth_1_dependancies = {}
    for key in dependancies.keys():
        version = dependancies.get(key)
        version = version.replace("^","")
        version = version.replace("~","")
        if not version == "*":
            status, package_dependancies = get_depenancies(key, version)
            if status == 200:
                depth_1_dependancies = {**depth_1_dependancies, **package_dependancies}
    return depth_1_dependancies
            
    

@app.route('/dependancy/', methods=['GET'])
def dependancy():
    if request.method == 'GET':
        messages = []
        results = []
        packageA = request.args.get('package-a')
        packageAVersion = request.args.get('package-a-version')
        packageB = request.args.get('package-b')
        packageBVersion = request.args.get('package-b-version')
        
        A_status, A_Depth_0_dependancies = get_depenancies(packageA, packageAVersion)
        B_status, B_Depth_0_dependancies = get_depenancies(packageB, packageBVersion)
        if not A_status == 200:
            if A_status == 404:
                messages.append(f"No package found for {packageA} - version {packageAVersion}")
            else:
                messages.append(f"omething went wrong while getting {packageA} - version {packageAVersion}")

        if not B_status == 200:
            if A_status == 404:
                messages.append(f"No package found for {packageB} - version {packageBVersion}")
            else:
                messages.append(f"omething went wrong while getting {packageB} - version {packageBVersion}")

        if not len(messages) > 0:
            A_Depth_1_dependancies = parse_depth_1_dependancies(A_Depth_0_dependancies)
            B_Depth_1_dependancies = parse_depth_1_dependancies(B_Depth_0_dependancies)
            common_ = A_Depth_1_dependancies.keys() & B_Depth_1_dependancies.keys()
            
            for key in common_:
                a_value = A_Depth_1_dependancies.get(key)
                b_value = B_Depth_1_dependancies.get(key)

                if "latest" in a_value or "next" in a_value:
                    adj = ""
                    if "latest" in a_value:
                        adj = "latest"
                    if "next" in a_value:
                        adj = "next"
                    sts, a_value = get_latest_version(key, adj)
                    if sts == 404:
                        a_value = A_Depth_1_dependancies.get(key)
                        
                if "latest" in b_value or "next" in b_value:
                    adj = ""
                    if "latest" in b_value:
                        adj = "latest"
                    if "next" in b_value:
                        adj = "next"
                    sts, b_value = get_latest_version(key, adj)
                    if sts == 404:
                        b_value = B_Depth_1_dependancies.get(key)
                
                chars_ = "^~"
                a_version = a_value.replace(chars_,"")
                b_version = b_value.replace(chars_,"")
                if not a_version == b_version:
                    if "latest" in a_version or "latest" in b_version:
                        results.append((key, a_value, b_value))
                    else:
                        if not a_version.split(".")[0] == b_version.split(".")[0]:
                            results.append((key, a_value, b_value))
                        elif not a_version.split(".")[1] == b_version.split(".")[1]:
                            results.append((key, a_value, b_value))
                        else:
                            pass
                            

    return render_template('dependancy.html', messages=messages, results=results, packageA=packageA, packageAVersion=packageAVersion, packageB=packageB, packageBVersion=packageBVersion)


if __name__ == "__main__":
    app.debug = True
    app.run()