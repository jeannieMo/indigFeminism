const homePageNames = {
    "1": {
        "id": "1",
        "name": "What is Indigenous Feminism?",
        "image": "/static/whatIsIndigFem.png",
        "Area": "Latin America",
        "summary": "Erin grew up in Hawaii, discovering her love of food while being raised with a deliciously diverse melting pot of flavors. Donny, a Cali native and dubbed “Farm Boy”, grew up on a ranch raising and imuing (deep pitting) pigs for Polynesian and Hispanic celebrations. Our roots are the foundation for the taste, quality and ingredients of Garden Creamery. We travel weekly together to handpick seasonal produce and herbs from local farms to create our flavors. We source our tea from select family farms in Japan and other parts of Asia. Here at our shop, we combine these fresh ingredients with 100% grass-fed, organic dairy from local Petaluma family farms. We also make a super creamy line of coconut-based vegan sorbet – sweetened with agave nectar, for a non-dairy alternative.",
        "similarTopics": {
            "Mitchells Ice Cream": "http://example.com/mitchells",
            "Miyako Old Fashioned Ice Cream": "http://example.com/miyako"
        },
        "webPage": 'http://127.0.0.1:5000/view/1'
    }
};
//help from chatgpt and stack overflow
$(document).ready(function(){
    for(x in homePageNames) {
        const clickableDiv = document.createElement('div');
        const nameSpan = document.createElement('span');
        nameSpan.textContent = homePageNames[x].name;
        nameSpan.style.fontWeight = 'bold'; 
        nameSpan.style.color = 'black'; 
       
        clickableDiv.appendChild(nameSpan);

        clickableDiv.classList.add('clickable-div');
        clickableDiv.addEventListener('click', handleClick(homePageNames[x].webPage));
        

        const imgColumn = document.createElement('div');
        imgColumn.classList.add('col-md-6'); // Set Bootstrap column class
        
        const img = document.createElement('img');
        img.src = homePageNames[x].image; 
        img.classList.add('img-fluid', 'smaller-image'); 
        imgColumn.appendChild(img);

        // Append both text and image columns to the same row
        const containerRow = document.getElementById('container-row');
        const textColumn = document.createElement('div');
        textColumn.classList.add('col-md-6'); // Set Bootstrap column class
        textColumn.appendChild(clickableDiv);
        containerRow.appendChild(textColumn);
        containerRow.appendChild(imgColumn);
    }     
//help from stack overflow
    document.getElementById('searchForm').reset()

    function handleClick(webPage) {
        return function() {
            redirectToInfoPage(webPage); 
        };
    }

    function redirectToInfoPage(url) {
        window.location.href = url;
    }


});

