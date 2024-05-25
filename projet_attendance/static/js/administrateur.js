function background_Green(element) {
  const checkbox = element.querySelector('input[type="checkbox"]')
  if (checkbox.checked) {
    element.style.backgroundImage = 'linear-gradient(to right, #006175 0%, #00a950 100%)';
  } else {

    element.style.background = '' 
  }
}
function checked(div) {
  const input = div.querySelector('input[type="checkbox"]');
  if (input) {
      input.checked = !input.checked;
      background_Green(div)
  }
}