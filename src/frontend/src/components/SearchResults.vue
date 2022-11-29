<template>
    <div class="card" style="color: rgb(0,0,0); width: 100%">
        <div class="card-body"
            style="display: flex;flex-direction: row;width: 100%;flex-wrap: nowrap;align-content: center;justify-content: flex-start;align-items: center;">
            <div class="col" style="margin-right: 0px;">
                <div class="row">
                    <div class="col">
                        <div class="row">
                            <h1 style="margin-bottom: 0px; font-family: Cabin; text-transform: uppercase; text-align: left;">
                                <em>{{ book.title }}</em>
                            </h1>
                            <h5 class="text-muted mb-2" style="font-family: Cabin; text-transform: uppercase; text-align: left;">
                                {{ authors }}</h5>
                            <p style="font-size: 14px;height: 200px;margin-bottom: 10px;width: 100%;text-align: justify;">
                                <span style="color: rgb(30, 25, 21);">{{ book.description }} [MORE]</span>
                            </p>
                        </div>
                        <div class="row">
                            <p class="flex-column justify-content-md-end"
                                style="font-size: 10px;margin-bottom: 0px;width: 100%;color: rgb(71,67,67);">
                                <em>This one is [RANDOM BUZZWORDS] and X% of readers have found it
                                    [RANDOM MOOD].</em><br>
                            </p>
                        </div>
                    </div>


                </div>

            </div>
            <div class="col text-center align-self-center"
                style="width: 100%;margin: 0px;margin-right: 10px;margin-left: 10px;">
                <img v-bind:src=book.cover_img
                    style="width: auto;height: 300px;box-shadow: 2px 2px 9px 2px rgba(0,0,0,0.26);" />
            </div>
        </div>
    </div>
</template>

<script lang="js" >
import { defineComponent } from 'vue';
import axios from "axios";
import router from '../router';

export default defineComponent({
    name: 'SearchResults',
    props: ['book'],
    components: {},
    data() {
        return {
            authors: ""
        }
    },
    setup() {
        return {};
    },
    mounted() {
        this.authors = this.book.author.join(", ");
    }
});
</script>