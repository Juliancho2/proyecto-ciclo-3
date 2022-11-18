<template>
    <div class="container_login">
        <div class="text_introduction">
            
            <h1>Compra y alquila los mejores<br> documentos digitales!</h1>
            <div>
                <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Error dolor mollitia sunt at sit, nam
                    voluptatum quos minus? Sint, harum blanditiis facilis veniam eum cumque corrupti recusandae
                    consectetur temporibus ullam consequuntur, non quo similique ipsum porro minima et soluta, itaque
                    odit magnam cum modi omnis quibusdam! Aliquid, veniam. Beatae .</p>
            </div>
        </div>
        <div class="form_container">
           
            <h2>Login</h2>
            <form @onSubmit.prevent="submit">
                <div class="form-group row my-2">
                    <label for="ussername" class="col-sm-2 col-form-label"><img src="../assets/kisspng-computer-icons-user-membership-vector-5b498fc79b8393.689490051531547591637.png" alt=""/></label>
                    
                    <div class="col-sm-6">
                        <input  type="text" required name="ussername" class="form-control" placeholder="username">
                    </div>
                </div>
                <div class="form-group row my-2">
                    <label for="password" class="col-sm-2 col-form-label"><img src="../assets/pngwing.com (2).png" alt=""></label>
                    <div class="col-sm-6">
                        <input type="password" required name="password" class="form-control" placeholder="password">
                    </div>
                </div>


                <button type="submit" class="btn btn-primary btn_login">Ingresar</button>

            </form>
        </div>

    </div>

</template>
<script setup>


</script>
<style scoped>
.container_login {
    box-sizing: border-box;
    display: grid;
    grid-template-columns: 1fr 1fr;
    width: 100%;
    min-height: 100vh;
}

.text_introduction {
    display: flex;
    flex-direction: column;
    padding: 50px;
    justify-content: center;
    /* background: url('../assets/texture-g6540fa2e2_19202.jpg') center/cover; */
    background: #0074B7;
}

.text_introduction h1 {
    line-height: 3rem;
    color: rgb(254, 254, 254);
    font-family: 'Rokkitt', serif;
    font-weight: 700;
    font-size: 3.5rem;
    
}
.text_introduction p{
    font-size: 1.2rem;
    color: rgb(230, 230, 225);
    font-family: 'Rokkitt', serif;
    line-height: 1rem;
    max-width: 25rem;
   
}

.text_introduction img{
    justify-self: unset;
}



form {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 10px;
   
}
.btn_login {
   max-width: 150px;
   align-self: flex-end;
}
form div input{
    width: 280px;
}

.form_container label img{
    max-width: 50px;
    max-height: 30px;
   
}

.form_container {
    background: rgb(245, 245, 245);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    margin: 0 auto;

}
@media (max-width:850px) {
    .container_login{
        grid-template-columns: 1fr;
        grid-template-rows:0.5fr 1fr;
    }
    .btn_login {
        align-self: flex-start;
    }
    
}
   
</style>