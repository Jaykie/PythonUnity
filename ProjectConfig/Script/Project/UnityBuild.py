#!/usr/bin/python
# coding=utf-8
import zipfile
import shutil
import os
import os.path
import time
import datetime
import sys
import subprocess
 
 
sys.path.append('../../') 
sys.path.append('./')  
from Config.Config import mainConfig
from Common import Source
from Config.AdConfig import mainAdConfig  
from Project.Resource import mainResource
from Common.File.FileUtil import FileUtil 
from Common.Platform import Platform
class UnityBuild(): 
# 主函数的实现
    @staticmethod
    def Run(stros):  
        # 0f6 2f1
        UNITYPATH=""
        if Platform.isWindowsSystem():
            UNITYPATH="E:/Unity/"+Source.UNITY_VERSION_WIN+"/Editor/Unity.exe"
            if not os.path.exists(UNITYPATH):
                # 阿里云添加环境变量 C:\Program Files\Unity\Hub\Editor\2019.3.2f1\Editor
                # UNITYPATH="C:/Program Files/Unity/Hub/Editor/"+source.UNITY_VERSION+"/Editor/Unity.exe"
                UNITYPATH= "Unity.exe"
        else:
            UNITYPATH="/Applications/Unity/Hub/Editor/"+Source.UNITY_VERSION_MAC+"/Unity.app/Contents/MacOS/Unity" 


        
        PROJECT_PATH= mainResource.GetRootProjectUnity()

        dirbin = mainResource.GetDirProduct()+"/bin"
        if stros == Source.ScreenShot:
            FileUtil.RemoveDir(dirbin)
        
        methond = ""
        if stros == Source.ANDROID:
            methond = "BuildPlayer.PerformAndroidBuild"
        if stros == Source.IOS:
            methond = "BuildPlayer.PerformiPhoneBuild"
        if stros == Source.ScreenShot:
            methond = "BuildPlayer.ScreenshotBuild"

            

        print("unity_build  start stros=",stros)
        cmd = UNITYPATH+" -quit "+" -batchmode "+" -projectPath "+PROJECT_PATH+" -executeMethod  "+methond
        # ps = subprocess.Popen(cmd)
        # ps.wait()#让程序阻塞
        os.system(cmd)
        print("unity_build  end")

        if stros == Source.ScreenShot: 
            if Platform.isWindowsSystem():
                cmd =  dirbin+"/game.exe"
            if Platform.isMacSystem():

                cmd =  "open "+dirbin+"/game.app"

            os.system(cmd)


# PROJECT_PATH="F:\sourcecode\unity\product\kidsgame\kidsgameUnity"

# companyName="moonma"
# productName="kidsgame"
# platform="0"
# outPath="F:\sourcecode\unity\product\kidsgame\project_android_output_cmd"
# arg0="参数谁便定义"
# E:\Program Files\Unity_All\2019.1.2f1\2019.1.2f1\Editor\Unity.exe -quit -batchmode -projectPath F:\sourcecode\unity\product\kidsgame\kidsgameUnity -executeMethod  ProjectBuild.BuildAndroid -buildTarget Android -exportPackage project_android_output_cmd kidsgame
# subprocess.call(UNITYPATH+" -quit "+" -batchmode "+" -projectPath "+PROJECT_PATH+" -executeMethod  ProjectBuild.BuildAndroid "+companyName+" "+productName+" "+platform+" "+outPath+" "+arg0)

# Unity.exe -quit -batchmode -projectPath F:\sourcecode\unity\product\kidsgame\kidsgameUnity -executeMethod  BuildPlayer.PerformAndroidUCBuild
#  os.system("adb connect "+myaddr)

