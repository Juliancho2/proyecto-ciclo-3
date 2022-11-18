<template>
    <div class="footer">
        <div>
            <svg class="editorial" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                viewBox="0 24 150 28" preserveAspectRatio="none">
                <defs>
                    <path id="gentle-wave" d="M-160 44c30 0 
    58-18 88-18s
    58 18 88 18 
    58-18 88-18 
    58 18 88 18
    v44h-352z" />
                </defs>
                <g class="parallax">
                    <use xlink:href="#gentle-wave" x="50" y="0" fill="#E4E5E8" />
                    <use xlink:href="#gentle-wave" x="50" y="3" fill="#E4E5E8" />
                    <use xlink:href="#gentle-wave" x="50" y="6" fill="#E4E5E8" />
                </g>

            </svg>

            <div class="container-grid">

                <div class="img-footer">
                    <img src="../assets/Documents.png" alt="" />
                </div>
                <div class="footer-item">
                    <p>
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Sequi ipsam tenetur similique
                        perferendis
                        cumque quasi delectus sit deserunt, saepe a.
                    </p>
                </div>
                <div class="footer-item">
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Obcaecati corporis pariatur, aperiam
                        ipsa maxime repudiandae magnam aliquid suscipit quasi error alias nesciunt, ipsum illo
                        voluptatum atque quis quas cum distinctio.</p>

                    
                </div>
                <div class="footer-item">
                    <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Beatae, quis. Neque quo beatae totam aliquam dolorum ipsa itaque, recusandae, excepturi vel iste quibusdam odit! Ullam corrupti porro iste dolorum cupiditate sunt soluta.,</p>


                </div>
            </div>
        </div>
    </div>
</template>

<script setup>

</script>

<style scoped>
.footer {
    position: relative;
    background: #F2F6F4;
    width: 100%;
    
}

.editorial {
    position: relative;
    bottom: 0px;

}

.container-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: 0.5fr 1fr ;
    background: #E4E5E8;

}

.img-footer {
    display: flex;
    justify-content: center;
    grid-column: 1/4;
}

.img-footer img {
    width: 100px;
    height: 50px;
}

.footer-item {
    display: flex;
    justify-content: center;
    /* background: red; */
    margin: 0 5px;

}

.footer-item p {
    width: 200px;
}

@media  (max-width:800px) {
    .container-grid {
        grid-template-columns: 1fr;
        grid-template-rows:  0.5fr 0.5fr 1fr ;
        
    }

    .img-footer {
        display: flex;
        justify-content: center;
        grid-column: 1/2;
    }
}
</style>