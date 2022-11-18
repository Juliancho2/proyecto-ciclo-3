<template>

    <div class="container">

        <div class="row">
            <div class="col text-left">
                <h2>Agregar documento</h2>
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
                                    <input type="text" required name="titulo" class="form-control"
                                        v-model.trim="form.titulo">
                                </div>
                            </div>

                            <div class="form-group row my-2">
                                <label for="tipo_doc" class="col-sm-2 col-form-label">Tipo documento</label>
                                <div class="col-sm-6">
                                    <!-- <input required class="form-control" type="text" name="tipo_doc"
                                        v-model.trim="form.tipo_doc"> -->
                                        <select class="form-select" name="" id="" v-model.trim="form.tipo_doc">
                                            <option value="Digital">Digital</option>
                                            <option value="Fisico">Fisico</option>
                                            <option value="Digital-fisico">Digital - fisico</option>

                                        </select>
                                </div>
                                
                            </div>



                            <div class="form-group row my-2">
                                <label for="nombre_autor" class="col-sm-2 col-form-label">Nombre autor</label>
                                <div class="col-sm-6">
                                    <input required class="form-control" type="text" name="nombre_autor"
                                        v-model.trim="form.nombre_autor">
                                </div>
                            </div>



                            <div class="form-group row my-2">
                                <label for="precio" class="col-sm-2 col-form-label">Precio</label>
                                <div class="col-sm-6">
                                    <input class="form-control" type="number" name="precio" v-model.trim="form.precio">
                                </div>
                            </div>
                            <div class="form-group row my-2">
                                <label for="categoria" class="col-sm-2 col-form-label">Categoria</label>
                                <div class="col-sm-6">

                                    <!-- <input required class="form-control" type="number" name="categoria"
                                        v-model.trim="form.fk_categoria"> -->
                                        <select v-model.trim="form.fk_categoria" class="form-select" name="" id="">
                                            <option value="1">Libro</option>
                                            <option value="2">Revista</option>
                                            <option value="3">Monografia</option>
                                            <option value="4">Ensayo</option>
                                            <option value="5">Iconografia</option>

                                        </select>

                                </div>
                            </div>
                            <div class="form-group row my-2">
                                <label for="tipo-doc" class="col-sm-2 col-form-label">Img url</label>
                                <div class="col-sm-6">
                                    <input required class="form-control" type="text" name="precio"
                                        v-model.trim="form.img_url">
                                </div>
                            </div>
                            <div class="row">
                                <div class="col text-left">
                                    <button type="submit" class="btn btn-primary mx-2">Agregar</button>
                                    <button class="btn btn-secondary" @click="sendOpen">Cancelar</button>
                                </div>

                            </div>
                        </form>





                    </div>
                </div>
            </div>
        </div>
    </div>


</template>
<script setup>

import { reactive, toRefs } from 'vue';
import swal from 'sweetalert'
const emit = defineEmits(['closeAdd']);

const props = defineProps({
    idItem: Object,

});
const { idItem } = toRefs(props);

const sendOpen = function (e) {
    emit('closeAdd', false);
    console.log(idItem)
}

const form = reactive(
    {
        titulo: "",
        nombre_autor: "",
        tipo_doc: 1,
        fk_categoria: 0,
        precio: "",
        img_url: ""
    }
);

const formInventory = reactive({
    fk_id_doc: "",
    cantidad_disponible: 5,
})


const onSubmit = function (e) {
    e.preventDefault();

    const path = `https://documentticapptic.onrender.com/api/productos/`;
    fetch(path, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(form)

    })
        .then(res => res.json())
        .then(response => {
            formInventory.fk_id_doc= response.id;
            location.href = '/inventario'
            emit('openChildren', false);
            swal("Documento agregado exitosamente!", "success");
            
        })
        .then(res => {
            
            fetch(`https://documentticapptic.onrender.com/api/inventario/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formInventory)
            })

        })
        .catch(err => swal("Ocurrio un error al agregar documento!", "error"))
}

</script>