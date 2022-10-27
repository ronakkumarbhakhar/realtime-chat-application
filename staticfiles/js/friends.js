var friendsbtn = document.querySelector( "#friendsbtn" );
var requestedbtn =document.querySelector( "#requestedbtn" );
var receivedbtn = document.querySelector( "#receivedbtn" );

friendsbtn.addEventListener("click", ()=> {
   
  let b= document.querySelector('#received')
  b.setAttribute("style", "display:None;");
  receivedbtn.classList.remove('active');

  let c= document.querySelector('#requested')
  c.setAttribute("style", "display:None;");
  requestedbtn.classList.remove('active');

  let a= document.querySelector('#friends')
  a.setAttribute("style", "display:flex;");
  friendsbtn.classList.remove('active');
  friendsbtn.classList.add('active');

});



receivedbtn.addEventListener("click", ()=>{
  let a= document.querySelector('#friends')
  a.setAttribute("style", "display:None;");
  friendsbtn.classList.remove('active');

  let c= document.querySelector('#requested')
  c.setAttribute("style", "display:None;");
  requestedbtn.classList.remove('active');

  let b= document.querySelector('#received')
  b.setAttribute("style", "display:flex;");
  receivedbtn.classList.remove('active');
  receivedbtn.classList.add('active');


});


var requestedbtn =document.querySelector( "#requestedbtn" );
requestedbtn.addEventListener("click", ()=>{
  let a= document.querySelector('#friends')
  a.setAttribute("style", "display:None;");
  friendsbtn.classList.remove('active');

  let b= document.querySelector('#received')
  b.setAttribute("style", "display:None;");
  receivedbtn.classList.remove('active');

  let c= document.querySelector('#requested')
  c.setAttribute("style", "display:flex;");
  requestedbtn.classList.remove('active');
  requestedbtn.classList.add('active');


});

  
var clickHandler =  (identity,url,textcontent)=>{
  let btn=document.querySelectorAll(identity)

  async function click(event){

    event.target.setAttribute("disabled", ""); 
    event.target.classList.remove("btn-primary")
    event.target.classList.add("btn-secondary")
    
    let friendId=event.target.getAttribute('data-friendId')

    await fetch(url+friendId)
    .then((res)=>{
      console.log(res);
      if(res.status==200)
      {
        event.target.textContent=textcontent;
      }
    })
  }

  for (var i = 0 ; i < btn.length; i++) 
  {
    btn[i].addEventListener('click',(event)=>{click(event)});
  }
    
   console.log("friends")

}






var chat_room_sent =  (identity)=>{
  let btn=document.querySelectorAll(identity)
  function click(event){

    event.target.classList.remove("btn-primary")
    
    let friendId=event.target.getAttribute('data-sentToId')

    url='friends/chat/'+friendId
    
    location.href=url;
  }

  for (var i = 0 ; i < btn.length; i++) {
    btn[i].addEventListener('click',(event)=>{click(event)});
 }
}



var chat_room_received =  (identity)=>{
  let btn=document.querySelectorAll(identity);
  function click(event)
  {

    event.target.setAttribute("disabled", ""); 
    event.target.classList.remove("btn-primary")
    event.target.classList.add("btn-secondary")
    
    let friendId=event.target.getAttribute('data-sentById')

    url='friends/chat/'+friendId
    
    location.href=url;
  }

  for (var i = 0 ; i < btn.length; i++)
  {
    btn[i].addEventListener('click',(event)=>{click(event)});
  }
}

clickHandler('.delete','friends/delete/','deleted');

clickHandler('.accept','friends/accept/','accepted');

chat_room_sent('.sent');

chat_room_received('.received');
