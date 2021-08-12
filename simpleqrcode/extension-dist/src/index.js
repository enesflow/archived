const qrCodeSize = 256;
const defaultdotsize = 75;
var url;
const qrcode = document.querySelector("#qrcode");
const urlInput = document.querySelector("#text");

let root = document.querySelector(":root");
root.style.setProperty("--qr-code-size", qrCodeSize + "px");
qrcode.addEventListener("mouseenter", (e) => {
	root.style.setProperty("--border-color", "lightcoral");
});
qrcode.addEventListener("mouseleave", (e) => {
	root.style.setProperty("--border-color", "black");
});

const getValue = (results, value) => {
	for (let j = 0; j < results.length; j++) {
		if (results[j][value] != null) {
			return results[j][value];
		}
	}
};

browser.tabs
	.query({
		currentWindow: true,
		active: true,
	})
	.then((tabInfo) => {
		url = tabInfo[0].url;
		urlInput.value = url;
	});

const main = async () => {
	async function sendMessageToTabs(tabs) {
		const response = await browser.tabs.sendMessage(tabs[0].id, {
			message: true,
		});
		return response;
	}

	const tabs = await browser.tabs.query({
		currentWindow: true,
		active: true,
	});
	urlInput.style.display = "none";
	url = urlInput.value || " ";
	document.querySelector("#alert").style.opacity = "0";

	setTimeout(() => {
		document.querySelector("#alert").style.opacity = "1";
	}, 2000);

	const results = await Promise.all([
		browser.storage.sync.get("customlogo"),
		browser.storage.sync.get("imageurl"),
		browser.storage.sync.get("urlshortener"),
		browser.storage.sync.get("websiteicon"),
	]);

	if ((getValue(results, "urlshortener") ?? true) && url.length > 100) {
		try {
			const shorturl = await axios.get(
				"https://tinyurl.com/api-create.php?url=" + url
			);
			url = shorturl.data;
		} catch {}
	}

	let logourl;
	if (getValue(results, "customlogo") ?? true) {
		if (getValue(results, "websiteicon") ?? true) {
			try {
				logourl = (await sendMessageToTabs(tabs)).message[0];
			} catch {}
		}
		if (!logourl) {
			if (getValue(results, "imageurl") != null) {
				if (getValue(results, "imageurl").length != 0) {
					logourl = getValue(results, "imageurl");
				} else {
					logourl = "chrome://branding/content/about-logo.png";
				}
			} else {
				logourl = "chrome://branding/content/about-logo.png";
			}
		}
	}

	let options = {
		data: url,
		type: "svg",
		imageOptions: {
			margin: 4,
		},
		margin: 0,
		width: qrCodeSize,
		height: qrCodeSize,
		dotsOptions: {
			color: "#333",
			type: "rounded",
		},
		qrOptions: {
			//If customlogo is disabled do not have a correctlevel
			errorCorrectionLevel:
				getValue(results, "customlogo") ?? true ? "Q" : "M",
		},
		//Check for customlogo
		image: logourl,
	};
	qrcode.innerHTML = "";
	await new QRCodeStyling(options).append(document.querySelector("#qrcode"));
	urlInput.style.display = "block";
};

document.addEventListener("DOMContentLoaded", main);
urlInput.addEventListener("input", main);
