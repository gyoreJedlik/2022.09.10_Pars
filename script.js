function VersenyValt(){
    ertek = parseInt (document.querySelector("#versenyek").value);
    kepNev = document.querySelector("#erem").src;
    switch(ertek){
        case 1:
            kepNev = "gold.png";
            title = "gold"
            break;
        case 2:
            kepNev = "silver.png";
            title = "silver"
            break;
        case 3:
            kepNev = "bronze.png";
            title = "bronze"
            break;
    }
    document.querySelector("#erem").src = kepNev;
}