<template>
    <WhiteHeader />

    <body id="page-top" data-bs-spy="scroll" data-bs-target="#mainNav" data-bs-offset="77"
        style="background: rgb(255,255,255); display: block; width: 100%;">
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
                                        <h3 class="text-center d-md-flex justify-content-md-center align-items-md-center" style="height: auto; color: rgb(0, 0, 0); width: auto;">
                                            {{ rating }}
                                        </h3>
                                        <FontAwesomeIcon icon="fa-star" style="color: black; font-size: 30px; margin-left: 5px;" />
                                    </div>
                                </div>
                                <div class="row" style="margin-top: 20px;">
                                    <div v-if="moods.length!=0" class="col text-start">
                                        <h6 class="text-start d-md-flex justify-content-md-center align-items-md-center"
                                            style="height: auto;width: auto;margin: 0px;margin-bottom: 5px;">
                                            <span style="color: rgb(0, 0, 0);">MOODS</span>
                                        </h6>
                                    </div>
                                    <p v-if="moods.length!=0"
                                        style="font-family: Arial;font-size: 13px;text-align: justify;padding: 5px;padding-top: 0px;padding-bottom: 0px;margin-bottom: 10px;">
                                        <span class="badge badge-dark" v-for="m in moods" style="background-color: #616161; margin: 2.5px;">
                                            {{ m }}
                                        </span>
                                    </p>
                                </div>
                            </div>
                            <div class="col">
                                <div class="row">
                                    <div class="col">
                                        <h1 class="text-start" style="color: rgb(0,0,0);margin: 0px; ">{{ title }}</h1>

                                        <h3 class="text-start" style="color: rgb(109,109,109);margin: 0px;margin-bottom: 15px;">
                                            {{ authors }}
                                            <button v-if="abstract!=null" class="btn btn-primary" @click="changeAbstract">
                                                <FontAwesomeIcon icon="fa-user" />
                                            </button>
                                        </h3>
                                        <p v-if="showAbstract" class="text-muted" style="font-size: 10px; text-align: justify;">
                                            {{ abstract }}
                                        </p>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col">
                                        <h6 class="text-start"
                                            style="color: rgb(194,194,194);margin: 0px;margin-bottom: 15px;">{{ genres }}
                                        </h6>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col">
                                        <h6 v-if="page_count != 0" class="text-start"
                                            style="color: rgb(50,50,50);margin: 0px;margin-bottom: 15px;">{{ page_count }}
                                            pages</h6>
                                        <h6 v-if="price != null" class="text-start"
                                            style="color: rgb(50,50,50);margin: 0px;margin-bottom: 15px;">{{ price }} €
                                        </h6>
                                    </div>
                                    <div class="col">

                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col" style="height: 311px;">
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
                                    <h1 class="text-start"
                                        style="margin: 0px;margin-bottom: 15px; color: rgb(0, 0, 0);">
                                        Reviews <h6 class="text-muted">({{ review_count }} total)</h6>
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
            <div class="row">
                <h1 class="text-start"
                                        style="margin: 0px;margin-bottom: 15px; color: rgb(0, 0, 0);">
                                        Similar Books
                                    </h1>

                                </div>

            <div class="row">
                <div class="col" style="margin-top: 25px;">
                    <div class="row">
                        <div class="col" id="similarDiv">
                            <SearchResults v-for="book in similar_books" :book="book" :key="book.id" />
                        </div>
                    </div>
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
import SearchResults from '../components/SearchResults.vue'

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
            pacing:"",
            buzzwords:[],
            mood:[],
            mood_percentage:[],
            moods:[],
            review:[],
            abstract: "",
            showAbstract: false,
            similar_books: []
      }
    },
    components: {
        WhiteHeader,
        Review,
        SearchResults
    },
    setup() {
        return {}
    },

    methods: {
        changeAbstract() {
            this.showAbstract = !this.showAbstract
        }
    },
    async created() {
        await axios.get('http://localhost:8080/book/' + this.$route.params.id).then((res) => {
            console.log(res.data);
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
            console.log(this.abstract);

            this.authors = this.author.join(", ");
            this.genres = this.genre.join(", ");

            var moods_array = this.mood_percentage[0].split(',');
            
            if(moods_array[0] != "[]"){
            for (var i = 0; i < moods_array.length; i++) {
                var number = moods_array[i].split(":")[1];
                number = number.split(",")[0];
                number = number.split("'")[0];
                console.log(number);
                number = Math.ceil(number * 100);
                console.log(number);
                if (number != 0) {
                    if (i == 0) {
                        this.moods.push(number + "% " + (moods_array[i].split(":")[0]).split("['")[1]);
                    }
                    else {
                        this.moods.push(number + "% " + (moods_array[i].split(":")[0]).split("'")[1]);
                    }
                }
                console.log("MOODS:", this.moods);
            }
        }

        });

        await axios.get('http://localhost:8080/similar/' + this.$route.params.id).then((res) => {
            console.log(res.data);
            this.similar_books = res.data;
        });



    }
})

</script>