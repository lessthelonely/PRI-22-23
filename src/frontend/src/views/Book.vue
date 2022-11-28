<template>
    <WhiteHeader />

    <body id="page-top" data-bs-spy="scroll" data-bs-target="#mainNav" data-bs-offset="77" style="background: rgb(255,255,255); display: block; width: 100%;">
        <div class="container">
            <div class="col">
                <div class="row">
                    <div class="col">
                        <div class="row" style="margin-bottom: 30px;">
                            <div class="col-md-5" style="width: 30%;">
                                <div class="row" style="margin-bottom: 15px;">
                                    <div class="col"> <img src="../assets/images/cover.jpg" style="width: 100%;font-size: 16px;">
                                        <h1 class="text-center d-md-flex justify-content-md-center align-items-md-center" style="height: auto;width: auto;margin: 0px;margin-bottom: 0px;">
                                            <span style="color: rgb(0, 0, 0); margin-top: 15px;">
                                                [X.X]
                                                <FontAwesomeIcon icon="fa-star" />
                                            </span>
                                        </h1>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col text-start">
                                        <h6 class="text-start d-md-flex justify-content-md-center align-items-md-center" style="height: auto;width: auto;margin: 0px;margin-bottom: 0px;">
                                            <span style="color: rgb(0, 0, 0);">MOODS</span>
                                        </h6>
                                    </div>
                                    <p style="font-family: Arial;font-size: 13px;text-align: justify;padding: 5px;padding-top: 0px;padding-bottom: 0px;margin-bottom: 10px;">
                                        <span style="color: rgb(0, 0, 0);">STATEMENT XX%</span>
                                    </p>
                                </div>
                            </div>
                            <div class="col">
                                <div class="row">
                                    <div class="col">
                                        <h1 class="text-start" style="color: rgb(0,0,0);margin: 0px; ">title</h1>
                                        <h3 class="text-start" style="color: rgb(109,109,109);margin: 0px;margin-bottom: 15px;">AUTHOR(S)
                                        </h3> </div>
                                </div>
                                <div class="row">
                                    <div class="col">
                                        <h6 class="text-start" style="color: rgb(194,194,194);margin: 0px;margin-bottom: 15px;">genres</h6> </div>
                                </div>
                                <div class="row">
                                    <div class="col" style="height: 311px;">
                                        <h6 class="text-start" style="color: rgb(0,0,0);margin: 0px;margin-bottom: 15px;">SYNOPSIS</h6>
                                        <p class="text-justify" style="font-family: Arial;color: rgb(0,0,0);font-size: 15px;height: 80%; text-align: justify;"> Description </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col flex-column">
                                <h1 class="text-start" style="margin: 0px;margin-bottom: 15px;"><span
                                    style="color: rgb(0, 0, 0);">reviews</span></h1>
                                <div>
                                    <div class="card" style="margin-bottom: 15px;">
                                        <div class="card-body">
                                            <p class="card-text" style="color: rgb(0,0,0);font-family: Arial;font-size: 13px;">Nullam id dolor id nibh ultricies vehicula ut id elit. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Donec id elit non mi porta gravida at eget metus. </p>
                                        </div>
                                    </div>
                                </div>
                            </div>
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

export default defineComponent({
    name: 'Book',
    components: {
        WhiteHeader
    },
    setup() {
        return {}
    },
})

</script>