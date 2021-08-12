function saveOptions(e) {
	e.preventDefault();
	browser.storage.sync.set({
		customlogo: document.querySelector("#customlogo").checked,
		imageurl: document.querySelector("#imageurl").value,
		urlshortener: document.querySelector("#urlshortener").checked,
		websiteicon: document.querySelector("#websiteicon").checked,
	});
}

function restoreOptions() {
	function setCurrentChoice(results) {
		document.querySelector("#customlogo").checked =
			results[0].customlogo ?? true;
		document.querySelector("#imageurl").value = results[1].imageurl ?? "";
		document.querySelector("#urlshortener").checked =
			results[2].urlshortener ?? true;
		document.querySelector("#websiteicon").checked =
			results[3].websiteicon ?? true;
	}

	function onError(error) {
		console.log(`Error: ${error}`);
	}

	Promise.all([
		browser.storage.sync.get("customlogo"),
		browser.storage.sync.get("imageurl"),
		browser.storage.sync.get("urlshortener"),
		browser.storage.sync.get("websiteicon"),
	]).then(setCurrentChoice);
}
document.addEventListener("DOMContentLoaded", restoreOptions);
const forminputs = document.querySelector("form").getElementsByTagName("input");
for (i = 0; i < forminputs.length; i++) {
	forminputs[i].oninput = saveOptions;
}
