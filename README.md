README.md

Components: github, ssh, server
The server is the Digital Ocean server, github is github, where the application files are stored, and ssh is the authentication method used to connect to the server. The username and password are stored in the Github Actions sectets. (In a real life scenario, SSH keys should be used instead of a password, as passwords are easier to obtain by malicious users.) After connecting to the server through the Github Actions, we can run any bash command in the scripts part of this solution.

3 problems encountered:
1: what method to use to connect:
	There are numerous ways to transfer files to a server (ftp, sftp, scp, and so on) and each of them comes with their own acript and own issues. I finally managed to do it by doing a pull request from the server. For this the initial git clone had to be set up on the server.
	
2: generating ssh-keys:
	While they were not used in the final solution, I did create and store an ssh key pair on both the server, it's authorized keys file and github.
	
3: fingerprint info:
	When connecting with ssh keys, fingerprint info was required from github. Solution was to run 
	ssh-keyscan github.com
	from my own pc and store the info in Github Actions secrets.
	
All in all, I wouldn't have minded if this assignment was a bit more detailed on the expectations. Am I only to achieve the goal in the eaisest way even if I know it would not cut it in a real world scenario? Should I be concerned about security issues? Bash scripting is listed, but is not really required for the solution. SSH connection via Github Actions is not very well documented in the first place, and on top, there are many available solutions on Github Action Marketplace that lack proper documentation in one way or another.
