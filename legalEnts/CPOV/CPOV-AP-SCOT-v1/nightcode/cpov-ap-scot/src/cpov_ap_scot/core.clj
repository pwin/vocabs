(ns cpov-ap-scot.core
  (:use [tawny owl pattern reasoner util]))


(def foaf "http://xmlns.com/foaf/0.1/")

(defontology dcat
  :iri "http://www.w3.org/ns/dcat")

(defclass Resource)

(defclass CatalogRecord)

(defclass Dataset
  :super Resource)

(defclass Document)

(defclass Catalog
  :super Dataset)

(reasoner-factory :hermit)

;;(consistent?)
;;(coherent?)

(save-ontology "dcat-v2.owl" :owl)