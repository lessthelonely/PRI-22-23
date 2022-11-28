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
                            <div class="col">
                                <div class="card" style="color: rgb(0,0,0);font-family: Arial;">
                                    <div class="card-body" style="display: flex; flex-direction: row;">
                                        <div class="col-md-8" style="width: 80%;margin-right: 0px;">
                                            <h1 style="margin-bottom: 0px;"><em>legendborn</em></h1>
                                            <h5 class="text-muted mb-2">tracy deonn</h5>
                                            <p
                                                style="font-size: 14px;height: 200px;margin-bottom: 10px;width: 100%;text-align: justify;">
                                                <span style="color: rgb(30, 25, 21);">After her mother dies in an
                                                    accident, sixteen-year-old Bree Matthews wants nothing to do with
                                                    her family memories or childhood home. A residential program for
                                                    bright high schoolers at UNC–Chapel Hill seems like the perfect
                                                    escape — until Bree witnesses a magical attack her very first night
                                                    on campus.&nbsp;&nbsp;A flying demon feeding on human
                                                    energies.&nbsp;A secret society of so called “Legendborn” students
                                                    that hunt the creatures down.&nbsp;And a mysterious teenage mage who
                                                    calls himself a “Merlin” and who attempts—and fails—to wipe Bree’s
                                                    memory of everything she saw... [MORE]</span><br></p>
                                            <p class="flex-column justify-content-md-end"
                                                style="font-size: 10px;margin-bottom: 0px;width: 100%;color: rgb(71,67,67);">
                                                <em>This one is [RANDOM BUZZWORDS] and X% of readers have found it
                                                    [RANDOM MOOD].</em><br></p>
                                        </div>
                                        <div class="col-md-4 text-center align-self-center"
                                            style="width: 10%;margin: 0px;margin-right: 10px;margin-left: 10px;">
                                            <img
                                                src="../assets/images/cover.jpg"
                                                style="width: auto;height: 300px;box-shadow: 2px 2px 9px 2px rgba(0,0,0,0.26);">
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

<script lang="js" >
import { defineComponent } from 'vue';
import WhiteHeader from '../components/WhiteHeader.vue';

export default defineComponent({
    name: 'Search',
    components: {
        WhiteHeader,
    },
    setup() {
        return {};
    },
});
</script>