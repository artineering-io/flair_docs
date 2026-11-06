// Before/after image sliders (.before-after with two <img>: before first, after second).
// Replaces the jQuery twentytwenty plugin of the old docs site. Without this script the two images
// show side by side (src/styles/content.css), so nothing is lost if it fails to run.
// A transparent range input covers the images, so dragging, clicking, touch and the keyboard all
// work without custom pointer handling. data-hover follows the mouse instead, like the old hero.
for (const box of document.querySelectorAll('.before-after')) {
	const [before, after] = box.querySelectorAll('img');
	if (!before || !after) continue;

	const slider = document.createElement('input');
	slider.type = 'range';
	slider.min = '0';
	slider.max = '100';
	slider.step = '0.1';
	slider.value = '50';
	slider.setAttribute('aria-label', 'Before/after comparison');
	const handle = document.createElement('span');
	handle.className = 'before-after__handle';
	handle.setAttribute('aria-hidden', 'true');
	box.append(slider, handle);

	for (const [img, key, side] of [
		[before, 'before', 'start'],
		[after, 'after', 'end'],
	]) {
		const text = box.dataset[key];
		if (!text) continue;
		const label = document.createElement('span');
		label.className = `before-after__label before-after__label--${side}`;
		label.textContent = text;
		box.append(label);
	}

	const set = (value) => box.style.setProperty('--position', `${value}%`);
	slider.addEventListener('input', () => set(slider.value));
	if (box.hasAttribute('data-hover')) {
		box.addEventListener('pointermove', (event) => {
			const rect = box.getBoundingClientRect();
			slider.value = String(((event.clientX - rect.left) / rect.width) * 100);
			set(slider.value);
		});
	}
	set(slider.value);
	box.classList.add('is-ready');
}
