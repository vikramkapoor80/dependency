Problem:
Dependency management can cause huge headaches for teams as they troubleshoot and resolve conflicting in first-order (1-layer deep) transient dependencies. This is especially true for large applications with sprawling dependency trees. In order to reduce the burden on individual teams and engineers, we’ve been asked to build an application that will allow engineers to quickly check for dependency collisions between NPM packages.

Task
Enhance the existing /dependency endpoint in the node server to check version conflicts in transient dependencies. The endpoint should, at a minimum, take in two package names and their versions (i.e. package_a at version_a, package_b at version_b). The endpoint should return a list of dependency conflict tuples containing package name and conflicting versions: [dependency_package_name, version_for_a, version_for_b]. Conflicts should be determined by dependency version mismatches between package_a and package_b.


Getting Started
To install dependencies and start the server in development mode:

Things to consider
Look at the inner "dependencies" object of a package for analysis of first-order dependencies.

npm returns dependency ranges that follow the Semantic Versioning specification, which you'll need to account for.

The packages update from time to time, just as their dependencies do.

What makes a good web service? API, performance, data storage, low latency, scalability, monitoring, a great web interface, you name it :)

Consider the quality and structure of your codebase; is it maintainable?

Consider production readiness (to some extent) and is it safe to deploy changes?
