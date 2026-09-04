# Mobile Agentic Testing Software
1. Downloaded Maestro, Android Studio, and Xcode. 
2. Downloaded Android 17 and iOS 16. 
3. Used iPhone 14 for iOS and Pixel 8 for Android. 
4. Created similar tests (YAML scripts) for both simulations on Maestro. The test entailed opening the Contacts app, attempting to add a new contact by entering a first and last name, canceling the changes, and exiting the app. 
5. Recorded both tests and saved the YAML scripts to this repository. 

### Made GenAI model to generate .yaml script with maestro commands from natural language. 
1. Use Gemma-4 to read test cases and give out a .yaml script that runs on maestro, the mobile app UI testing software.
2. Made a modular system prompt containing a detailed list of instructions to give to model.
3. Stored information regarding the maestro commands along with examples of such .yaml scripts in .md files belonging to modular_prompt folder. 
4. Then I made a function to compile all these markdown files to make one cohesive system prompt. 
5. Finally, I made a function to save the generated output to a .yaml file. 
