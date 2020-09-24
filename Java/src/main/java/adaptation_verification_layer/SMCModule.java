package adaptation_verification_layer;
import specification.*;
import java.util.ArrayList;

public class SMCModule {
    private SampleGenerator sampler;
    private Simulator simulator;
    private Verifier verifier;

    public VerificationResult verifyAdaptationTactic(SystemModel sys, AdaptationTactic tactic, EnvironmentPrediction prediction, AdaptationGoal goal){
        //todo: specify your SMC algorithms (SMCS, SSP, SPRT, etc.)
        ArrayList<SimulationResult> simResults = new ArrayList<SimulationResult>();

        while(!isSufficient()){
            //iterate sample generation, simulation, and addition of the simulation result
            //step 3
            EnvironmentData sample = sampler.generateSample(prediction);

            //step 4
            simResults.add(simulator.simulate(sys, tactic, sample));
        }

        //step 5
        return verifier.verify(simResults, goal);
    }

    private boolean isSufficient(){
        //todo: implement SMC algorithm's sample-sufficiency-checking method
        return true;
    }
}
