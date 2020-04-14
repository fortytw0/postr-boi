var all_index_cards = Array.from(document.querySelectorAll(".index-card"));
console.log(all_index_cards);
// var all_bg_imgs = document.querySelectorAll(".index-card .post-bg-img");
// console.log(all_bg_imgs);

// global variables


// event listeners

// window.addEventListener('load' , hideBackgroundImagesOnLoad);

all_index_cards.forEach(function(index_card){
    index_card.addEventListener('mousedown' , function(e){
        console.log(e)
        showBackgroundOnHover(index_card)
    })
    index_card.addEventListener('mouseup' , function(e){
        console.log(e)
        revertBackgroundAfterHover(index_card)
    })
})



// function definitions


function showBackgroundOnHover(index_card)
{   

    console.log(index_card)
    index_card.querySelector(".post-content").hidden = true
    index_card.querySelector(".post-author-tags").hidden = true
    index_card.querySelector(".post-stats").hidden = true

    index_card.querySelector(".post-bg-img").hidden = false

    console.log("showBackgroundOnHover")
}

function revertBackgroundAfterHover(index_card) 

{
    index_card.querySelector(".post-content").hidden = false
    index_card.querySelector(".post-author-tags").hidden = false
    index_card.querySelector(".post-stats").hidden = false

    index_card.querySelector(".post-bg-img").hidden = true

    console.log("revertBackgroundAfterHover")


}
