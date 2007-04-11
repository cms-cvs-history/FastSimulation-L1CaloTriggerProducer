#ifndef L1CaloTriggerProducer_FastL1CaloSim_h
#define L1CaloTriggerProducer_FastL1CaloSim_h
// -*- C++ -*-
//
// Package:    L1CaloTriggerProducer
// Class:      FastL1CaloSim
// 
/**\class FastL1CaloSim FastL1CaloSim.h FastSimulation/L1CaloTriggerProducer/src/FastL1CaloSim.h

 Description: Fast Simulation of the L1 Calo Trigger.

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Chi Nhan Nguyen
//         Created:  Mon Feb 19 13:25:24 CST 2007
// $Id: FastL1CaloSim.h,v 1.2 2007/03/09 17:08:34 chinhan Exp $
//
//

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FastSimulation/L1CaloTriggerProducer/interface/FastL1GlobalAlgo.h"

//
// class decleration
//
class FastL1CaloSim : public edm::EDProducer {
   public:
      explicit FastL1CaloSim(const edm::ParameterSet&);
      ~FastL1CaloSim();


      virtual void produce(edm::Event&, const edm::EventSetup&);
   private:
      // ----------member data ---------------------------
      FastL1GlobalAlgo* m_L1GlobalAlgo;
};

#endif