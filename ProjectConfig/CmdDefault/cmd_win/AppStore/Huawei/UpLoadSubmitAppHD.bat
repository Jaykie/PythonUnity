
  
@set filepath = %~dp0 

cd ../../../../../../../Common/PythonUnity/ProjectConfig/Script

python AppStoreManager.py %~dp0 UpdateApk huawei hd
python AppStoreManager.py %~dp0 UpdateVersion huawei hd


@Pause

 


 
 