<template>
    <WhiteHeader />

    <body id="page-top" data-bs-spy="scroll" data-bs-target="#mainNav" data-bs-offset="77"
        style="background: rgb(255,255,255); display: block; width: 100%; height: auto;">
        <div class="container">
            <div class="col">
                <div class="row">
                    <div class="col">
                        <div class="row" style="margin-bottom: 30px;">
                            <div class="col-md-5" style="width: 30%; display: flex; flex-direction: column;">
                                <div class="row" style="margin-bottom: 30px;">
                                    <div class="col">
                                        <img v-bind:src="cover_img"
                                            style="width: 100%;font-size: 16px; box-shadow: 2px 2px 9px 2px rgb(0 0 0 / 26%);">
                                    </div>
                                </div>
                                <div class="row" style="text-align: center; display: flex; justify-content: center;">
                                    <div class="col" style="text-align: center; display: flex; justify-content: center;">
                                        <h3 class="text-center d-md-flex justify-content-md-center align-items-md-center"
                                            style="height: auto; color: rgb(0, 0, 0); width: auto;">
                                            {{ rating }}
                                        </h3>
                                        <FontAwesomeIcon icon="fa-star"
                                            style="color: black; font-size: 30px; margin-left: 5px;" />
                                    </div>
                                </div>
                                <div class="row" style="margin-top: 20px;">
                                    <div v-if="moods.length != 0" class="col text-start">
                                        <h6 class="text-start d-md-flex justify-content-md-center align-items-md-center"
                                            style="height: auto;width: auto;margin: 0px;margin-bottom: 5px;">
                                            <span style="color: rgb(0, 0, 0);">MOODS</span>
                                        </h6>
                                    </div>
                                    <p v-if="moods.length != 0"
                                        style="font-family: Arial;font-size: 13px;text-align: justify;padding: 5px;padding-top: 0px;padding-bottom: 0px;margin-bottom: 10px;">
                                        <span class="badge badge-dark" v-for="m in moods"
                                            style="background-color: #616161; margin: 2.5px;">
                                            {{ m }}
                                        </span>
                                    </p>
                                </div>
                            </div>
                            <div class="col">
                                <div class="row">
                                    <div class="col">
                                        <h1 class="text-start" style="color: rgb(0,0,0);margin: 0px; ">{{ title }}</h1>

                                        <h3 class="text-start" style="color: rgb(109,109,109);margin: 0px;margin-bottom: 15px; display: flex; flex-wrap: nowrap; flex-direction: row;">
                                            <div v-for="a in author">
                                                <router-link class="text-start author-link" :to="{ name: 'Author', params: { name: a }}" @click="goToAuthorPage(a)" v-if="(author.indexOf(a) != (author.length - 1))">
                                                    {{ a + ","}}
                                                </router-link>
                                                <router-link class="text-start author-link" :to="{ name: 'Author', params: { name: a }}" @click="goToAuthorPage(a)" v-else >
                                                    {{ a }}
                                                </router-link>
                                            </div>
                                        </h3>
                                        <p v-if="showAbstract" class="text-muted"
                                            style="font-size: 10px; text-align: justify;">
                                            {{ abstract }}
                                        </p>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col">
                                        <h6 class="text-start"
                                            style="color: rgb(194,194,194);margin: 0px;margin-bottom: 15px;">{{ genres
                                            }}
                                        </h6>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col">
                                        <h6 v-if="page_count != 0" class="text-start"
                                            style="color: rgb(50,50,50);margin: 0px;margin-bottom: 15px;">{{ page_count
                                            }}
                                            pages</h6>
                                        <h6 v-if="price != null" class="text-start"
                                            style="color: rgb(50,50,50);margin: 0px;margin-bottom: 15px;">{{ price }} €
                                        </h6>
                                    </div>
                                    <div class="col">

                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col" style="height: fit-content;">
                                        <h6 class="text-start"
                                            style="color: rgb(0,0,0);margin: 0px;margin-bottom: 15px;">SYNOPSIS</h6>
                                        <p class="text-justify"
                                            style="font-family: Arial;color: rgb(0,0,0);font-size: 18px;height: 80%; text-align: justify;">
                                            {{ description }} </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col flex-column">
                                <div class="row">
                                    <h1 class="text-start" style="margin: 0px;margin-bottom: 15px; color: rgb(0, 0, 0);">
                                        Reviews
                                    </h1>
                                </div>

                                <div v-if="review.length != 0">
                                    <Review v-for="review in review" :text="review" />
                                </div>
                                <p style="font-family: Arial;color: rgb(0,0,0);font-size: 18px;text-align: justify;"
                                    v-else>
                                    No available reviews.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col" v-if="(similar_books.length != 0)">
                <div class="row">
                    <h1 class="text-start" style="margin: 0px;margin-bottom: 15px; color: rgb(0, 0, 0);">
                        Similar Books
                    </h1>
                </div>
                <div class="row">
                    <div class="col" id="similar-results-1" v-if="(page == 1)" style="display: flex; width: 100%; overflow: hidden; flex-direction: row; flex-wrap: nowrap; align-content: center; justify-content: center; align-items: center;">
                        <SimilarResults v-bind:cover_img="book.cover_img" v-bind:buzzwords="book.buzzwords.toString()"
                            v-bind:id="book.id" v-bind:mood="book.mood.toString()" v-bind:rating="book.rating"
                            v-for="book in similar_books.slice(0, 5)"
                            v-if="(similar_books.slice(0, 5).length != 0)" />
                            <p style="font-family: Arial;color: rgb(0,0,0);font-size: 18px;text-align: justify;" v-else>
                                No more suggestions available.
                            </p>
                    </div>

                    <div class="col" id="similar-results-2" v-if="(page == 2)" style="display: flex; width: 100%; overflow: hidden; flex-direction: row; flex-wrap: nowrap; align-content: center; justify-content: center; align-items: center;">
                        <SimilarResults v-bind:cover_img="book.cover_img" v-bind:buzzwords="book.buzzwords.toString()"
                            v-bind:id="book.id" v-bind:mood="book.mood.toString()" v-bind:rating="book.rating"
                            v-for="book in similar_books.slice(5, 10)" v-if="(similar_books.slice(5, 10).length != 0)" />
                            <p style="font-family: Arial;color: rgb(0,0,0);font-size: 18px;text-align: justify;" v-else>
                                No more suggestions available.
                            </p>
                    </div>

                    <div class="col" id="similar-results-3" v-if="(page == 3)" style="display: flex; width: 100%; overflow: hidden; flex-direction: row; flex-wrap: nowrap; align-content: center; justify-content: center; align-items: center;">
                        <SimilarResults v-bind:cover_img="book.cover_img" v-bind:buzzwords="book.buzzwords.toString()"
                            v-bind:id="book.id" v-bind:mood="book.mood.toString()" v-bind:rating="book.rating"
                            v-for="book in similar_books.slice(10, 15)" v-if="(similar_books.slice(10, 15).length != 0)"/>
                            <p style="font-family: Arial;color: rgb(0,0,0);font-size: 18px;text-align: justify;" v-else>
                                No more suggestions available.
                            </p>
                    </div>
                    <ul>
                        <li>
                            <button class="btn btn-primary" @click="back()">
                                <FontAwesomeIcon icon="fa-arrow-left" />
                            </button>
                            <button class="btn btn-primary" @click="next()">
                                <FontAwesomeIcon icon="fa-arrow-right" />
                            </button>
                        </li>
                    </ul>
                    
                </div>
            </div>
        </div>
    </body>
</template>

<script lang="js">
import { defineComponent } from 'vue'
import WhiteHeader from '../components/WhiteHeader.vue'
import Review from '../components/Review.vue'
import axios from 'axios'
import SimilarResults from '../components/SimilarResults.vue'

export default defineComponent({
    name: 'Book',
    data() {
        return {
            author: [],
            authors: "",
            book_format: [],
            description: "",
            genre: [],
            genres: "",
            cover_img: "",
            title: "",
            isbn: "",
            page_count: 0,
            rating: 0,
            review_count: 0,
            price: 0,
            sensitivity: [],
            pacing: "",
            buzzwords: [],
            mood: [],
            mood_percentage: [],
            moods: [],
            review: [],
            abstract: "",
            showAbstract: false,
            similar_books: [],
            page: 1,
        }
    },
    components: {
        WhiteHeader,
        Review,
        SimilarResults
    },
    setup() {
        return {}
    },

    methods: {
        changeAbstract() {
            this.showAbstract = !this.showAbstract
        },

        next() {
            if (this.page < 3) {
                this.page += 1
            }
        },

        back() {
            if (this.page > 1) {
                this.page -= 1
            }
        },

        goToAuthorPage(name) {
            window.location.href = "/author/" + name;
        }
    },
    async created() {
        await axios.get('http://localhost:8080/book/' + this.$route.params.id).then((res) => {
            this.author = res.data.author
            this.book_format = res.data.book_format
            this.description = res.data.description
            this.genre = res.data.genre
            this.cover_img = res.data.cover_img
            this.title = res.data.title
            this.isbn = res.data.isbn
            this.page_count = res.data.page_count
            this.rating = res.data.rating
            this.review_count = res.data.review_count
            this.price = res.data.price
            this.sensitivity = res.data.sensitivity
            this.pacing = res.data.pacing
            this.buzzwords = res.data.buzzwords
            this.mood = res.data.mood
            this.mood_percentage = res.data.mood_percentage
            this.review = res.data.review
            this.abstract = res.data.abstract

            this.authors = this.author.join(", ");
            this.genres = this.genre.join(", ");

            if(this.mood_percentage != "[]"){
                for(var i=0; i<this.mood_percentage.length; i++){
                    var temp_array = this.mood_percentage[i].split(":");
                    var temp_number=0;
                    if(i==this.mood_percentage.length-1){
                        temp_number = temp_array[1].split("]")[0];
                        temp_number=Math.ceil(temp_number*100);
                    }
                    else{
                        temp_number=Math.ceil(temp_array[1]*100);
                    }
                    if(temp_number != 0){
                        if(i==0){
                            this.moods.push(temp_number + "% " + (this.mood_percentage[i].split(":")[0]).split("['")[1].split("'")[0]);
                        }
                        else{
                            this.moods.push(temp_number + "% " + (this.mood_percentage[i].split(":")[0]).split("'")[1]);
                        }
            }
            }
    }
        });

        await axios.get('http://localhost:8080/similar/' + this.$route.params.id).then((res) => {
            this.similar_books = res.data;
        });



    }
})

</script>