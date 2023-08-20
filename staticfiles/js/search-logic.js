"use strict"

let searchBtn=document.querySelector('.search-fig');
let searchQuery= document.querySelector('.search');
searchBtn.addEventListener('click',(event)=>{
    if(searchQuery.value==""){
        return false;
    }
    else{
        let value= searchQuery.value;
        console.log(searchQuery.length);
        searchQuery.value="";
        window.location.assign(`/search?search=${value}`);
    }
})