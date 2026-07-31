QUANTUM LOVE - ANDROID APP

This project is ready to compile into an Android APK.

FASTEST BUILD METHOD - GITHUB
1. Create a new GitHub repository.
2. Upload ALL files and folders from this QuantumLove folder, including the .github folder.
3. Open the repository's Actions tab.
4. Select "Build Android APK".
5. Run the workflow if it did not start automatically.
6. When the build finishes, open the workflow run and download the artifact named "QuantumLove-Android-APK".
7. Extract the downloaded artifact ZIP. The .apk inside can be transferred to an Android phone and installed.

NOTE
Android may ask you to allow installation from your browser/file manager because this is a locally built debug APK and is not from Google Play.

LOCAL LINUX BUILD
Install Buildozer and Android dependencies, then run:
    buildozer android debug
The APK will be created inside the bin folder.
