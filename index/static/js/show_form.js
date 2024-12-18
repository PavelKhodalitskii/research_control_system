const createButton = document.getElementById("create_button")
const containerToShow = document.getElementById("appering_form_contianer")
const closeButton = document.getElementById("close_button")

const showSideMenu = () => {
    if (containerToShow.style.display != 'none') {
        containerToShow.style.display = 'none';
    } else {
        containerToShow.style.display = 'block';
    }
};

createButton.addEventListener("click", showSideMenu);
closeButton.addEventListener("click", showSideMenu);