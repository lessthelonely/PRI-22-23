<template>
    <WhiteHeader />

    <body id="page-top" data-bs-spy="scroll" style="background: rgb(255,255,255); display: block; width: 100%;">
        <div class="container">
            <div class="col">
                <div class="row">
                    <div class="col-lg-xl">
                        <input type="text" id="input-query"
                            style="width: 80%; font-family: Cabin; border-radius: 10px; height: 50px; padding: 10px; font-size: 20px;"
                            placeholder="Put your query here." v-on:keyup.enter="search()" autocomplete="off"
                            v-model="term" @input="filterTerms" @focus="modal = true" />
                        <button
                            style="width: 2%; text-align:center; background-color: transparent; font-size: 10px; margin-left: -40px;"
                            @click="clearSuggestions">
                            <FontAwesomeIcon icon="angle-double-up" />
                        </button>

                        <button class="btn btn-primary" style="width: 5%; font-size: 20px; margin-left: 30px;"
                            @click="search">
                            <FontAwesomeIcon icon="fa-search" />
                        </button>
                        <button class="btn btn-primary" style="width: 5%; font-size: 20px; margin-left: 15px;"
                            @click="showAdvancedInputs">
                            <FontAwesomeIcon icon="angle-double-down" />
                        </button>

                        <div class="autocom-box" style="position: absolute; z-index: 1; width: 73%;">
                            <ul style="font-size: 12px; margin-left: 50px; background-color: #F3F6F6;" v-if="modal">
                                <li class="text-black"
                                    style="color: black; font-size: 12px; width: fit-content; background: transparent; margin-left: -30px;"
                                    v-for="term in terms" @click="setTerm(term)">
                                    {{ term }}
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="row" id="advanced-filters" v-if="showAdvanced" style="margin-top: 15px; display: flex; flex-direction: column; align-content: center; align-items: center; justify-content: center; flex-wrap: nowrap;">
                    <button id="add-button" style="margin-bottom: 20px; width: 50px; height: 40px; align-items: center; display: flex; justify-content: center; align-content: center; flex-direction: column; flex-wrap: nowrap;"
                        @click="addFilter">
                        <FontAwesomeIcon icon="fa-plus" />
                    </button>

                    <AdvancedFilter name="advanced-filter-1" />
                </div>
            </div>


            <p v-if="spelling != ''" class="text-muted" style="margin-left: 50px; margin-top: 10px; display: float; background: white;  z-index: 2; color: black; text-align: left; font-size: 16px;">
                Did you mean
                <button id="button-search" @click="correctSearch">
                    {{ spelling }}
                </button>?
            </p>

            <div class="row" style="margin-top: 15px;">
                <div class="col">
                    <div class="row" style="display: flex; flex-direction: row;">
                        <div class="col" style="max-width: 137px;">
                            <p style="display:float; color:black; text-align: left;">
                                More Important:
                            </p>
                        </div>
                        <div class="col" style="text-align: left;">
                            <div style="margin-right: 10px; align-items: center; display: inline-flex; lex-direction: row; flex-wrap: nowrap; align-content: center; justify-content: center;">
                                <input type="checkbox" @click="addWeights('title')" id="title" 
                                    style="display:float; text-align: left;" />
                                <label for="title" style="color:black;">Title</label>
                            </div>
                            <div style="margin-right: 10px; align-items: center; display: inline-flex; lex-direction: row; flex-wrap: nowrap; align-content: center; justify-content: center;">
                                <input type="checkbox" @click="addWeights('author')" id="author" 
                                    style="display:float; text-align: left;" />
                                <label for="author" style="color:black;">Author</label>
                            </div>
                            <div style="margin-right: 10px; align-items: center; display: inline-flex; lex-direction: row; flex-wrap: nowrap; align-content: center; justify-content: center;">
                                <input type="checkbox" @click="addWeights('price')" id="price" 
                                    style="display:float; text-align: left;" />
                                <label for="price" style="color:black;">Price</label>
                            </div>
                            <div style="margin-right: 10px; align-items: center; display: inline-flex; lex-direction: row; flex-wrap: nowrap; align-content: center; justify-content: center;">
                                <input type="checkbox" @click="addWeights('sensitivity')" id="sensitivity"
                                     style="display:float; text-align: left;" />
                                <label for="sensitivity" style="color:black;">Sensitivity</label>
                            </div>
                            <div style="margin-right: 10px; align-items: center; display: inline-flex; lex-direction: row; flex-wrap: nowrap; align-content: center; justify-content: center;">
                                <input type="checkbox" @click="addWeights('mood')" id="mood" 
                                    style="display:float; text-align: left;" />
                                <label for="mood" style="color:black;">Moods</label>
                            </div>
                            <div style="margin-right: 10px; align-items: center; display: inline-flex; lex-direction: row; flex-wrap: nowrap; align-content: center; justify-content: center;">
                                <input type="checkbox" @click="addWeights('buzzwords')" id="buzzwords"
                                     style="display:float; text-align: left;" />
                                <label for="buzzwords" style="color:black;">Buzzwords</label>
                            </div>
                            <div style="margin-right: 10px; align-items: center; display: inline-flex; lex-direction: row; flex-wrap: nowrap; align-content: center; justify-content: center;">
                                <input type="checkbox" @click="addWeights('book_format')" id="book_format"
                                     style="display:float; text-align: left;" />
                                <label for="book_format" style="color:black;">Format</label>
                            </div>
                            <div style="margin-right: 10px; align-items: center; display: inline-flex; lex-direction: row; flex-wrap: nowrap; align-content: center; justify-content: center;">
                                <input type="checkbox" @click="addWeights('genre')" id="genre" 
                                    style="display:float; text-align: left;" />
                                <label for="genre" style="color:black;">Genre</label>
                            </div>
                            <input type="checkbox" @click="addWeights('rating')" id="rating" 
                                style="display:float; text-align: left;" />
                            <label for="rating" style="color:black;">Rating</label>
                        </div>

                    </div>
                    <div class="col" style="margin-top: 25px;">
                        <div class="row">
                            <div class="col" id="searchResultsDiv">
                                <SearchResults v-for="book in pageBooks" :book="book" :key="book.id" />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="mb-4 d-flex justify-content-center">
    <pagination
      v-model="currentPage"
      :records="totalPages"
      :per-page="perPage"
      @paginate="pageChanged" 
      :hideCount="true"
    />
  </div>
    </body>
</template>

<script lang="js" >
import { defineComponent, createApp } from 'vue';
import pagination from "v-pagination-3";
import axios from "axios";
import WhiteHeader from '../components/WhiteHeader.vue';
import SearchResults from '../components/SearchResults.vue';
import AdvancedFilter from '../components/AdvancedFilter.vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';


export default defineComponent({
    name: 'Search',
    components: {
        WhiteHeader,
        SearchResults,
        AdvancedFilter,
        pagination
    },
    data() {
        return {
            books: [],
            pageBooks:[],
            showAdvanced: false,
            spelling: "",
            term: "",
            modal: false,
            terms: [],
            weights: [],
            filterCount: 2,
            currentPage: 1,
            perPage: 10,
            totalPages: 100
        }
    },
    methods: {
        pageChanged(page){
            this.currentPage = page;
            this.pageBooks = this.books.slice((page-1)*this.perPage, page*this.perPage);
        },
        async filterTerms() {
            console.log("TERM: ", this.term);

            var term = this.term.toLowerCase();
            if (term.includes("/")) {
                term = term.replace("/", "&");
            }

            this.terms = [];
            if (this.term.length != "") {
                await axios.get("/suggestions/" + term).then((response) => {
                    for (var i = 0; i < response.data.length; i++) {
                        this.terms.push(response.data[i].term);
                    }
                });
            }

        },

        clearSuggestions() {
            this.terms = [];
        },

        addWeights(id) {
            var checkbox = document.getElementById(id);
            if (checkbox.checked) {
                this.weights.push(checkbox.id);
            }
            else {
                this.weights.splice(this.weights.indexOf(checkbox.id), 1);
            }
        },

        async setTerm(term) {
            this.term = term;
            document.getElementById("input-query").value = term;
            this.modal = false;

            var term = this.term.toLowerCase();
            if (term.includes("/")) {
                term = term.replace("/", "&");
            }

            //this.search();

            await axios.get("/suggestion-search/" + term).then((response) => {
                this.books = response.data;
                this.pageChanged(1);
            });
        },

        async search() {
            this.modal = false;
            var query = document.getElementById("input-query").value;
            console.log("SEARCH ", query);

            var selects = document.querySelectorAll(".filter-select");
            var filters = [];
            for (var i = 0; i < selects.length; i++) {
                filters.push(selects[i].value);
            }

            var inputs = document.querySelectorAll(".filter-input");
            var values = [];
            for (var i = 0; i < inputs.length; i++) {
                if ((inputs[i].value) == "") {

                    filters.pop();
                }
                if ((inputs[i].value).includes("<")) {
                    var strInt = (inputs[i].value).split("<");
                    var range = "[0 TO " + strInt[1] + "]";
                    values.push(range);
                }
                else if ((inputs[i].value).includes("-")) {
                    var strInt = (inputs[i].value).split("-");
                    var range = "[" + strInt[0] + " TO " + strInt[1] + "]";
                    values.push(range);
                }
                else {
                    values.push(inputs[i].value);
                }
            }

            console.log(filters, values);

            if (filters.length == 0 && values.length == 0) {
                console.log("no filters");
                query = query.toLowerCase();
                if (query.includes("/")) {
                    query = query.replace("/", "&");
                }
                console.log("SEARCHING: ", query);
                console.log(query);
                console.log("/search/" + query);
                if (this.weights.length == 0) {
                    await axios.get("/search/" + query).then((response) => {
                        this.books = response.data;
                        this.pageChanged(1);
                        console.log(this.books);
                        if (this.books[0]['spellcheck'] != null) {
                            this.spelling = this.books[0]['spellcheck'];
                            console.log("SPELLING: ", this.spelling);
                        }
                    });
                }
                else {
                    var weighted_term = '';
                    for (var i = 0; i < this.weights.length; i++) {
                        weighted_term += this.weights[i] + " ";
                    }
                    await axios.get("/search-weighted/" + query + "/" + weighted_term).then((response) => {
                        this.books = response.data;
                        this.pageChanged(1);
                        if (this.books[0]['spellcheck'] != null) {
                            this.spelling = this.books[0]['spellcheck'];
                            console.log("SPELLING: ", this.spelling);
                        }
                    });
                }

            }
            else {

                var jsonData = {};
                for (var i = 0; i < filters.length; i++) {
                    jsonData[filters[i]] = values[i];
                    console.log(jsonData);
                }

                console.log(jsonData);

                await axios.post("/filter-search", jsonData).then((response) => {
                    this.showAdvanced = false;
                    this.books = response.data;
                    this.pageChanged(1);
                    console.log(this.books);
                });

            }
        },

        showAdvancedInputs() {
            console.log(this.books[0]);
            this.showAdvanced = !this.showAdvanced;
        },

        addFilter() {
            var searchBar = document.getElementById("advanced-filters");
            var filterApp = createApp(AdvancedFilter, {name: 'advanced-filter-' + this.filterCount});
            this.filterCount++;
            filterApp.component('FontAwesomeIcon', FontAwesomeIcon);
            
            var filterElem = filterApp.mount(document.createElement('div')).$el;
            searchBar.appendChild(filterElem);
        },

        async correctSearch() {
            this.term = this.spelling;
            document.getElementById("input-query").value = this.spelling;
            await axios.get("/search/" + this.spelling).then((response) => {
                this.books = response.data;
                this.spelling = "";
                this.pageChanged(1);
            });
        }
    },
    created() {
        document.title = "Search";
    },
    async mounted() {
        await axios.get('http://localhost:8080/books').then((response) => {
            this.books = response.data;
        });
        this.pageBooks = this.books.slice(0, this.perPage);
    }
});
</script>