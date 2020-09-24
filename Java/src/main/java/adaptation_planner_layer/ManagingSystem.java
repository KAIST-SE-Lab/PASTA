package adaptation_planner_layer;

import adaptation_verification_layer.SMCModule;
import data_analysis_layer.ForecastingEngine;
import interaction_layer.Actuators;
import interaction_layer.Sensors;
import knowledge_layer.AdaptationGoalManager;
import knowledge_layer.EnvironmentDatabase;
import knowledge_layer.SystemModelManager;
import knowledge_layer.TacticRepository;
import specification.*;

import java.util.ArrayList;
import java.util.HashMap;

public class ManagingSystem {
    //Knowledge
    private EnvironmentDatabase envDB;
    private SystemModelManager sysModelManager;
    private TacticRepository tacticRepo;
    private AdaptationGoalManager goalManager;

    //Data analysis layer
    private ForecastingEngine forecaster;

    //Interaction layer
    private Sensors sensors;
    private Actuators actuators;

    //Adaptation verification layer
    private SMCModule SMC;

    public ManagingSystem(){
        //todo: initialize your SAS
        envDB = new EnvironmentDatabase();
        SystemModel SASmodel = new SystemModel();
        sysModelManager = new SystemModelManager(SASmodel);
        ArrayList<AdaptationTactic> tactics = new ArrayList<AdaptationTactic>();
        tacticRepo = new TacticRepository(tactics);
        AdaptationGoal goal = new AdaptationGoal();
        goalManager = new AdaptationGoalManager(goal);

        forecaster = new ForecastingEngine();

        sensors = new Sensors();
        actuators = new Actuators();

        SMC = new SMCModule();
    }

    public void adaptManagedSystem(){
        //step 1
        EnvironmentData monitoredData = sensors.monitor();
        envDB.addEnvironmentData(monitoredData);
        sysModelManager.updateModel();

        //step 2
        EnvironmentPrediction prediction = forecaster.forecast(envDB.getHistoricalEnvironmentData());

        //step 3, 4, and 5 - work as "Optimal adaptation tactic searching module"
        HashMap<AdaptationTactic, VerificationResult> evaluations = new HashMap<AdaptationTactic, VerificationResult>();
        SystemModel sys = sysModelManager.getSysModel();
        AdaptationGoal goal = goalManager.getGoal();
        for(AdaptationTactic tactic : tacticRepo.getPossibleTactics()){
            evaluations.put(tactic, SMC.verifyAdaptationTactic(sys, tactic, prediction, goal));
        }

        //step 6
        AdaptationTactic selectedTactic = getOptimalTactic(evaluations);

        //step 7
        actuators.execute(selectedTactic);
    }

    private AdaptationTactic getOptimalTactic(HashMap<AdaptationTactic, VerificationResult> evaluations){
        //todo: implement how to find optimal tactic
        AdaptationTactic optimalTactic = null;
        //find optimal one among evaluation sheets.

        return optimalTactic;
    }
}
