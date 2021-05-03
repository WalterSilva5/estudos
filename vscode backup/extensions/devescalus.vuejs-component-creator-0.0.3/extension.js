// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
const vscode = require("vscode");
const fs = require("fs");
const path = require("path");

function getComponentNameFromUser() {
  return vscode.window.showInputBox({
    placeHolder: "component-name",
  });
}
function clearAndUpper(text) {
  return text.replace(/-/, "").toUpperCase();
}

function toPascalCase(text) {
  return text.replace(/(^\w|-\w)/g, clearAndUpper);
}
// this method is called when your extension is activated
// your extension is activated the very first time the command is executed

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
  let disposable = vscode.commands.registerCommand(
    "vuejs-component-creator.createComponent",
    async function (e) {
      let selectedFolderPath = e.fsPath;
      let indexJs = `export default {
			components: { },
			data() {
				return {

				}
			},
			methods: {

			},
		}`;

	  let vueTpl = `<template></template><script src="./index.js"></script><style src="./index.scss" lang="scss"></style>`;

      const componentName = await getComponentNameFromUser();

      fs.promises
        .mkdir(`${selectedFolderPath}/${componentName}`)
        .then(() => {
          fs.writeFile(
            path.join(`${selectedFolderPath}/${componentName}`, "index.js"),
            indexJs,
            (err) => {
              if (err) {
                return vscode.window.showErrorMessage(
                  "Failed to create boilerplate file!"
                );
              }
            }
          );
          fs.writeFile(
            path.join(`${selectedFolderPath}/${componentName}`, "index.scss"),
            "",
            (err) => {
              if (err) {
                return vscode.window.showErrorMessage(
                  "Failed to create boilerplate file!"
                );
              }
              fs.writeFile(
                path.join(
                  `${selectedFolderPath}/${componentName}`,
                  `${toPascalCase(componentName)}.vue`
                ),
                vueTpl,
                (err) => {
                  if (err) {
                    return vscode.window.showErrorMessage(
                      "Failed to create boilerplate file!"
                    );
                  }
                }
              );
            }
          );
        })
        .catch(console.error);
      // Display a message box to the user
      vscode.window.showInformationMessage("Component created");
    }
  );

  context.subscriptions.push(disposable);
}
exports.activate = activate;

// this method is called when your extension is deactivated
function deactivate() {}

module.exports = {
  activate,
  deactivate,
};
