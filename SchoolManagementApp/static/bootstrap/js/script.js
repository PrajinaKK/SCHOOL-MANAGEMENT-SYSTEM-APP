const radios = document.querySelectorAll('.radio');

radios.forEach(radion => {
    radion.addEventListener('change', function(){
        document.querySelectorAll('.radio-circle').forEach(div => {
            div.classList.remove('selected')
        });

        if(this.checked){
            this.closest('.radio-circle').classList.add('selected')
             
        }    
    });
});