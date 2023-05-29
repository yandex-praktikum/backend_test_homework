chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
    if (changeInfo.favIconUrl) {
      chrome.tabs.executeScript(tabId, {
        code: "var link = document.querySelector('link[rel=\"shortcut icon\"]') || document.createElement('link'); link.type = 'image/x-icon'; link.rel = 'shortcut icon'; link.href = '" + changeInfo.favIconUrl + "'; document.getElementsByTagName('head')[0].appendChild(link);"
      });
    }
  });  
