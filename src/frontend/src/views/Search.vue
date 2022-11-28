<template>
    <WhiteHeader />
    <body id="page-top" data-bs-spy="scroll" style="background: rgb(255,255,255); display: block; width: 100%;">
        <div class="container">
            <div class="col">
                <div class="row">
                    <div class="col"><input type="text"
                            style="width: 100%;font-family: Arial;border-radius: 10px;height: 50px;padding: 10px;font-size: 20px;"
                            placeholder="Put your query here."></div>
                </div>
                <div class="row">
                    <div class="col" style="margin-top: 25px;">
                        <div class="row">
                            <div class="col" id="searchResultsDiv">
                                <SearchResults v-for="book in books" :book="book" :key="book.id" />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
</template>

<script lang="js" >
import { defineComponent, createApp } from 'vue';
import axios from "axios";
import WhiteHeader from '../components/WhiteHeader.vue';
import SearchResults from '../components/SearchResults.vue';

export default defineComponent({
    name: 'Search',
    components: {
        WhiteHeader,
        SearchResults
    },
    data(){
        return {
            books: [],
        }
    },
    setup() {
        return {};
    },
    async mounted(){
        await axios.get('http://localhost:8080/books').then((response)=>{
            this.books = response.data;
        });

       
    }
});
</script>