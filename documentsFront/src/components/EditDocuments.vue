<template>

    <div class="container">
        
        <div class="row">
            <div class="col text-left">
                <h2>Editar documento</h2>
            </div>
        </div>

        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <form @submit="onSubmit">
                            <div class="form-group row my-2">
                                <label for="titulo" class="col-sm-2 col-form-label">Titulo</label>
                                <div class="col-sm-6">
                                    <input type="text" required name="titulo" class="form-control" v-model.trim="form.titulo">
                                </div>
                            </div>

                            <div class="form-group row my-2">
                                <label for="tipo_doc" class="col-sm-2 col-form-label">Tipo documento</label>
                                <div class="col-sm-6">
                                    <input class="form-control" type="text" name="tipo_doc"
                                        v-model.trim="form.tipo_doc">
                                </div>
                            </div>



                            <div class="form-group row my-2">
                                <label for="nombre_autor" class="col-sm-2 col-form-label">Nombre autor</label>
                                <div class="col-sm-6">
                                    <input class="form-control"  required type="text" name="nombre_autor"
                                        v-model.trim="form.nombre_autor">
                                </div>
                            </div>



                            <div class="form-group row my-2">
                                <label for="precio" class="col-sm-2 col-form-label">Precio</label>
                                <div class="col-sm-6">
                                    <input class="form-control" required type="number" name="precio" v-model.trim="form.precio">
                                </div>
                            </div>
                            <div class="form-group row my-2">
                                <label for="categoria" class="col-sm-2 col-form-label">Categoria: 1-libro, 2-revista, 3-monografia, 4-ensayo,5-iconografia</label>
                                <!-- <span ></span> -->
                                <div class="col-sm-6">
                                    
                                    <input class="form-control" required type="number" name="categoria" min="1" max="5" v-model.trim="form.fk_categoria">
                                    
                                </div>
                            </div>
                            <div class="form-group row my-2">
                                <label for="tipo-doc" class="col-sm-2 col-form-label">Img url</label>
                                <div class="col-sm-6">
                                    <input class="form-control" required type="text" name="precio" v-model.trim="form.img_url">
                                </div>
                            </div>
                            <div class="row">
                                <div class="col text-left">
                                    <button type="submit" class="btn btn-primary mx-2">Editar</button>
                                    <button class="btn btn-secondary" @click="sendOpen()">Cancelar</button>
                                </div>

                            </div>
                        </form>





                    </div>
                </div>
            </div>
        </div>
    </div>
   

</template>
<script  setup>
import { onMounted, toRefs , reactive } from 'vue';
import swal from 'sweetalert'

const props= defineProps({
    idItem:Object,

});

const { idItem } = toRefs(props);
const emit=defineEmits(['openChildren']);

const form=reactive(
    {
        titulo:"",
        nombre_autor:"",
        tipo_doc:1,
        fk_categoria:0,
        precio:"",
        img_url:""
}
)

const sendOpen=function(){
   emit('openChildren',false);
}
const getEditDocument= function(){

    const path = `https://documentticapptic.onrender.com/api/productos/${idItem.value.id}/`;
    fetch(path)
        .then(res => res.json())
        .then(response => {
            
            form.titulo= response.titulo
            form.nombre_autor = response.nombre_autor;
            form.tipo_doc= response.tipo_doc;
            form.fk_categoria=response.fk_categoria;
            form.precio =response.precio;
            form.img_url=response.img_url;
            
        }).catch(err => console.log(err));

};
const onSubmit=function(e){
        e.preventDefault();
        const path = `https://documentticapptic.onrender.com/api/productos/${idItem.value.id}/`;
        fetch(path,{
        method: 'PUT',
        headers:{
            'Content-Type': 'application/json'
        },
        body:JSON.stringify(form)

    })
    .then(res=>res.json())
    .then(response=>{
        
        location.href= '/inventario'
        emit('openChildren',false);
        
      })
    .catch(err=>swal("Ocurrio un error al actualizar documento!", "error"))
}

onMounted(()=>{
    getEditDocument();
});






</script>
<style scoped>

</style>