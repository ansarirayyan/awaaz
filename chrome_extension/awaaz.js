console.clear()
function refreshData() {
function interceptType() {
	var scr = document.createElement('script');
	scr.type = 'text/javascript'
	scr.innerHTML = `
    async function sendT(latestMsg) {
    	return fetch("http://127.0.0.1:42069/",{
    		method: 'POST',
    		body: latestMsg
    	})
    }
    function checkVariable() {
    	if(typeof document.getElementsByClassName("messageContent-2qWWxC")[49] !== 'undefined') {
    		console.debug(document.getElementsByClassName("messageContent-2qWWxC")[49].innerText)
    		sendT(document.getElementsByClassName("messageContent-2qWWxC")[49].innerText);
    	} else {
    		setTimeout(checkVariable, 250);
    	}
    }
    setTimeout(checkVariable, 250);
`
	document.head.prepend(scr);
}
function checkForDOM() {
  if (document.body && document.head) {
    interceptType();
  } else {
    requestIdleCallback(checkForDOM);
  }
}
requestIdleCallback(checkForDOM);

setTimeout(refreshData, 100);

}

refreshData();
