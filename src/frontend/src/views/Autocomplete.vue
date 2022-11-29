<template>
<div class="about flex flex-col items-center">
    <div class="bg-red-300 absolute inset-0"></div>
    <input type="text" class="bg-gray-300 px-4 py-2" autocomplete="off" v-model="state" @input="filterStates" @focus="modal=true">

    <div v-if="filteredStates && modal">
        <ul class="w-48 bg-gray-800">
            <li style="background:black;" class="py-2 border-b cursor-pointer" v-for="state in terms" @click="setState(state)">
                {{ state }}
            </li>
        </ul>
    
    </div>
</div>
</template>


<script lang="js">
import { defineComponent } from 'vue';
import axios from "axios";

    export default defineComponent({
        name: 'Autocomplete',
        components:{},
        data(){
            return{
                state: "",
                states: [
                    'Florida', 'Alabama', 'Alaska','Texas'
                ],
                filteredStates: [],
                modal: false,
                terms:[]
            }
        },
        methods:{
            async filterStates(){
                ///suggestions/{query}
                console.log(this.state);
                this.terms=[];
                await axios.get("/suggestions/"+this.state).then((response) => {
                    for (var i = 0; i < response.data.length; i++) {
                        this.terms.push(response.data[i].term);
                    }
                });

            },
            setState(state){
                this.state = state;
                this.modal = false;
            }
        }
      
    });
</script>







