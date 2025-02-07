Let me help you troubleshoot your MkDocs configuration with the mike plugin for versioning. Based on your configuration, there are a few things we need to check:

First, make sure mike is properly installed:

bashCopypip install mike

You need to initialize and deploy a version before it will show up. Here are the steps:

bashCopy# Initialize git repository if you haven't already
git init

# Build and deploy your first version
mike deploy 1.0 latest

# Set default version
mike set-default latest

# Serve the documentation locally
mike serve
Note: Don't use mkdocs serve directly when using mike - use mike serve instead. This is because mkdocs serve won't show the version selector since it bypasses the versioning system.
Also, check that:

Your repository has at least one commit
You're using the material theme correctly (which I see you are)
The version selector should appear in the header of your documentation

If you're still not seeing the version selector after following these steps, could you tell me:

What command are you using to serve the documentation locally?
Have you deployed any versions using mike yet?