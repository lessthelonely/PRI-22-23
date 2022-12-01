<template>
    <WhiteHeader />

    <body id="page-top" data-bs-spy="scroll" style="background: rgb(255,255,255); display: block; width: 100%;">
        <div class="container">
            <div class="col">
                <div class="row">
                    <div class="col-lg-xl" >
                        <input type="text" id="input-query"
                            style="width: 80%; font-family: Cabin; border-radius: 10px; height: 50px; padding: 10px; font-size: 20px;"
                            placeholder="Put your query here." v-on:keyup.enter="search()" autocomplete="off" v-model="term" @input="filterTerms" @focus="modal=true"/>
                       
                        <button class="btn btn-primary" style="width: 5%; font-size: 20px; margin-left: 15px;"
                            @click="search">
                            <FontAwesomeIcon icon="fa-search" />
                        </button>
                        <button class="btn btn-primary" style="width: 5%; font-size: 20px; margin-left: 15px;"
                            @click="showAdvancedInputs">
                            <FontAwesomeIcon icon="angle-double-down" />
                        </button>

                        <div class="autocom-box" style="position: absolute; z-index: 1; width: 66%;" >
                            <ul style="font-size: 12px; margin-left: 50px; background-color: #F3F6F6;" v-if="modal">
                                <li class="text-black" style="color: black; font-size: 12px; width: fit-content; background: transparent; margin-left: -30px;" v-for="term in terms" @click="setTerm(term)">
                                    {{ term }}
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="row" v-if="showAdvanced" style="margin-top: 15px; display: flex; flex-direction: column; align-content: center; align-items: center; justify-content: center; flex-wrap: nowrap;">
                    <button id="add-button" style="margin-bottom: 20px; width: 50px; height: 40px; align-items: center; display: flex; justify-content: center; align-content: center; flex-direction: column; flex-wrap: nowrap;" @click="addFilter">
                            <FontAwesomeIcon icon="fa-plus" />
                        </button>
                    <div class="col" id="search-bar">
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
            <p v-if="spelling!=''" class="text-muted" style="margin-left: 50px; margin-top: 10px; display: float; background: white;  z-index: 2; color: black; text-align: left; font-size: 16px;"> Did you mean <button id="button-search" @click="correctSearch"> {{spelling}} </button>?</p>
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
            showAdvanced: false,
            spelling: "",
            term: "",
            modal: false,
            terms: []
        }
    },
    methods: {
        async filterTerms(){
            console.log("TERM: ",this.term);
            
            this.terms=[];
                await axios.get("/suggestions/"+this.term).then((response) => {
                    for (var i = 0; i < response.data.length; i++) {
                        this.terms.push(response.data[i].term);
                    }
                });
            
        },
        setTerm(term){
            this.term=term;
            document.getElementById("input-query").value=term;
            this.modal=false;
            this.search();
        },
        async search() {
            this.modal=false;
            var query = document.getElementById("input-query").value;
            console.log("SEARCH ",query);

            var selects = document.querySelectorAll(".filter-select");
            var filters = [];
            for (var i = 0; i < selects.length; i++) {
                filters.push(selects[i].value);
            }

            var inputs = document.querySelectorAll(".filter-input");
            var values = [];
            for (var i = 0; i < inputs.length; i++) {
                if((inputs[i].value)== ""){

                    filters.pop();
                }
                if((inputs[i].value).includes("<")){
                    var strInt = (inputs[i].value).split("<");
                    var range = "[0 TO "+ strInt[1] +"]";
                    values.push(range);
                }
                else if((inputs[i].value).includes("-")){
                    var strInt = (inputs[i].value).split("-");
                    var range = "["+ strInt[0] +" TO "+ strInt[1] +"]";
                    values.push(range);
                }
                else{
                    values.push(inputs[i].value);
                }            
            }

            console.log(filters, values);

            if(filters.length==0 && values.length==0){
                console.log("no filters");
                query = query.toLowerCase();
                if(query.includes("/")){
                    query = query.replace("/","&");
                }
                console.log("SEARCHING: ", query);
                console.log(query);
                console.log("/search/"+query);
                await axios.get("/search/"+query).then((response) => {
                    this.books = response.data;
                    console.log(this.books);
                    if(this.books[0]['spellcheck']!=null){
                        this.spelling = this.books[0]['spellcheck'];
                        console.log("SPELLING: ", this.spelling);
                    }
                });
            }
            else{

                var jsonData = {};
                for (var i = 0; i < filters.length; i++) {
                    jsonData[filters[i]] = values[i];
                    console.log(jsonData);
                }

                console.log(jsonData);

                await axios.post("/filter-search", jsonData).then((response) => {
                    this.showAdvanced = false;
                    this.books = response.data;
                    console.log(this.books);
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
        },

        async correctSearch(){
            await axios.get("/search/"+this.spelling).then((response) => {
                    this.books = response.data;
                    this.spelling="";
                });
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