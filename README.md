# Introduction

This repository contains code to accompany my [How To Use Transformers To Automatically Generate Stories In Rasa] blog post on Medium.

# Prerequisites
1. Docker
2. VS Code

# Usage

1. Open this project in a container
2. Train a model with `rasa train`
3. Run the rasa server with `make run-rasa-server`
4. Run the nlg server with `make run-nlg-server`
5. Preview the [bot_ui.html](bot_ui.html) file to chat with the bot