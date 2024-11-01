function footerAdjust(){
    footer = document.getElementById("footer") ;
    body = document.getElementsByTagName("body");
    body = body[0];
    
    if(body.offsetHeight > screen.height){
        footer.classList.add("footer-adjust")
    }
}
footerAdjust();