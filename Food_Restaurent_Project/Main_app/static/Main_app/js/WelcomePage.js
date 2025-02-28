const dynamicPara = document.querySelector(".dynamicPara");
dynamicPara.innerText = " "
const foodDeliveryHighlights = [
    "Craving? We've Got You Covered!",
    "Explore Local Favorites!",
    "Variety at Your Fingertips!",
    "Fast, Fresh, and Reliable!",
    "Easy Ordering, Zero Hassle!",
    "Exclusive Offers Just for You!",
    "Track Your Feast in Real-Time!",
    "Safe & Contactless Delivery!"
  ];


const showHighLight = (sentence) => {
    let index = 0
    dynamicPara.innerText = " ";

    const intervalId = setInterval(() => {
        if (index < sentence.length) {
          dynamicPara.innerText += sentence[index];
          index++;
        }
        else {
            clearInterval(intervalId);
        }
        }, 100);

};

const getHighlight = () => {
    const highLightSentenceIndex = Math.round(Math.random() * foodDeliveryHighlights.length);
    const highLightSentence = foodDeliveryHighlights[highLightSentenceIndex];
    showHighLight(highLightSentence);
}

getHighlight();
setInterval(getHighlight, 5000);