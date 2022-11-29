<template>
    <WhiteHeader />

    <body id="page-top" data-bs-spy="scroll" style="background: rgb(255,255,255); display: block; width: 100%;">
        <div class="container">
            <div class="col">
                <div class="row">
                    <div class="col-lg-xl">
                        <input type="text" id="input-query"
                            style="width: 80%; font-family: Cabin; border-radius: 10px; height: 50px; padding: 10px; font-size: 20px;"
                            placeholder="Put your query here." v-on:keyup.enter="search()" />
                        <button class="btn btn-primary" style="width: 5%; font-size: 20px; margin-left: 15px;"
                            @click="search">
                            <FontAwesomeIcon icon="fa-search" />
                        </button>
                        <button class="btn btn-primary" style="width: 5%; font-size: 20px; margin-left: 15px;"
                            @click="showAdvancedInputs">
                            <FontAwesomeIcon icon="angle-double-down" />
                        </button>
                    </div>
                </div>
                <div class="row" v-if="showAdvanced" style="margin-top: 15px;">
                    <div class="col" id="search-bar">
                        <button id="add-button" style="margin-right: 15px;" @click="addFilter">
                            <FontAwesomeIcon icon="fa-plus" />
                        </button>
                        <select class="filter-select" placeholder="Attribute"
                            style="font-family: Cabin; padding: 10px;">
                            <option value="author">Author</option>
                            <option value="book_format">Format</option>
                            <option value="ISBN">ISBN</option>
                            <option value="page_count">Page Count</option>
                            <option value="rating">Rating</option>
                            <option value="review_count">Review Count</option>
                            <option value="title">Title</option>
                            <option value="price">Price</option>
                            <option value="sensitivity">Sensitivity</option>
                            <option value="pacing">Pacing</option>
                            <option value="buzzwords">Buzzwords</option>
                            <option value="mood">Moods</option>
                        </select>
                        <input class="filter-input" type="text" style="font-family: Cabin; margin-left: 15px; padding: 10px;" />
                    </div>
                </div>
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
    data() {
        return {
            books: [],
            showAdvanced: false
        }
    },
    methods: {
        async search() {
            console.log("hewwo");

            const query = document.getElementById("input-query").value;
            console.log(query);

            var selects = document.querySelectorAll(".filter-select");
            var filters = [];
            for (var i = 0; i < selects.length; i++) {
                filters.push(selects[i].value);
            }

            var inputs = document.querySelectorAll(".filter-input");
            var values = [];
            for (var i = 0; i < inputs.length; i++) {
                values.push(inputs[i].value);
            }

            console.log(filters, values);

            if(filters.length==0 && values.length==0){
                console.log("no filters");
                await axios.get("/search/"+query).then((response) => {
                    this.books = response.data;
                });
            }
        },

        showAdvancedInputs() {
            console.log(this.books[0]);
            this.showAdvanced = !this.showAdvanced;
        },

        addFilter() {
            var searchBar = document.getElementById("search-bar");

            var col = "<div class='col' style='margin-top: 10px;'> <select class='filter-select' placeholder='Attribute' style='font-family: Cabin; padding: 10px;'> <option value='author'>Author</option> <option value='book_format'>Format</option> <option value='ISBN'>ISBN</option> <option value='page_count'>Page Count</option> <option value='rating'>Rating</option> <option value='review_count'>Review Count</option> <option value='title'>Title</option> <option value='price'>Price</option> <option value='sensitivity'>Sensitivity</option> <option value='pacing'>Pacing</option> <option value='buzzwords'>Buzzwords</option> <option value='mood'>Moods</option> </select> <input class='filter-input' type='text' style='margin-left: 15px; font-family: Cabin; padding: 10px;' /></div>";
            searchBar.innerHTML += col;
        }
    },
    setup() {
        return {};
    },
    async mounted() {
        await axios.get('http://localhost:8080/books').then((response) => {
            this.books = response.data;
        });
    }
});
</script>