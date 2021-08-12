browser.runtime.onMessage.addListener((request) => {
	const result = [];
	[
		'link[rel="apple-touch-icon"]',
		'link[rel="icon"]',
		'meta[name="msapplication-TileImage"]',
		'meta[property="og:image"]',
	].forEach((i) => {
		if (document.querySelector(i)) {
			result.push(
				document.querySelector(i).href ??
					document.querySelector(i).content
			);
		}
		if (document.querySelector('meta[name="msapplication-config"]')) {
			console.log(
				document.querySelector('meta[name="msapplication-config"]')
					.content
			);
		}
	});
	console.log(request.message);
	return Promise.resolve({
		message: result,
	});
});
