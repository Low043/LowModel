from github import Github
import requests, os, sys

class VersionManager:
    def __init__(self,currentVersion,updateFromRepo,accessToken=None):#None token for public repos
        self.currentVersion = currentVersion#Version must be last release name
        self.connection = Github(accessToken)
        self.repository = self.__getRepo(updateFromRepo)#updateFromRepo must be 'owner/repo'
        self.token = accessToken
        self.latestVersion, self.assets = self.__getLastRelease()

    def __getRepo(self,repo):
        return self.connection.get_repo(repo)
    
    def __getLastRelease(self):
        try:
            latestRelease = self.repository.get_latest_release()
            return (latestRelease.title,latestRelease.get_assets()[0])
        except:
            return (self.currentVersion,None)
        
    def update(self):
        headers = {'Authorization' : f'token {self.token}','Accept' : 'application/octet-stream'}#Default settings to get private repos
        executable = requests.get(self.assets.url,stream=True,headers=headers)
        open('updatedFile.exe','wb').write(executable.content)

    def close(self):
        self.connection.close()