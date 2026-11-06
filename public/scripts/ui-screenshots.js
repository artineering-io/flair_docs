// UI screenshots (figure.aio-ui) are captured on high-DPI screens, so they're shown at 70% of their
// pixel size to match the size of the real interface. CSS can't read an image's pixel size, so
// this runs once each image has loaded. Ported from the old docs site. It sets width, not max-width,
// so the stylesheet's max-width: 100% still caps the image on narrow screens.
for (const img of document.querySelectorAll('figure.aio-ui img')) {
	const fit = () => {
		img.style.width = `${img.naturalWidth * 0.7}px`;
	};
	if (img.complete) fit();
	else img.addEventListener('load', fit, { once: true });
}
