# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/circuit_analysis.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cproto/circuit_analysis.proto\x12\x08\x62igspicy\")\n\x03Net\x12\x13\n\x0bsignal_name\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\x04\"-\n\x0fSimulatedDriver\x12\x1a\n\x03net\x18\x01 \x01(\x0b\x32\r.bigspicy.Net\"=\n\x0e\x43\x61pacitiveLoad\x12\x1a\n\x03net\x18\x01 \x01(\x0b\x32\r.bigspicy.Net\x12\x0f\n\x07value_f\x18\x02 \x01(\x01\"$\n\x06\x44\x43\x42ias\x12\x1a\n\x03net\x18\x01 \x01(\x0b\x32\r.bigspicy.Net\"*\n\x0cVoltageProbe\x12\x1a\n\x03net\x18\x01 \x01(\x0b\x32\r.bigspicy.Net\"F\n\x0c\x41nalysisPort\x12\x1a\n\x03net\x18\x01 \x01(\x0b\x32\r.bigspicy.Net\x12\x1a\n\x12load_capacitance_f\x18\x02 \x01(\x01\"\x9e\x03\n\x0c\x44\x65signRegion\x12\x0c\n\x04name\x18\x01 \x01(\t\x12<\n\x08\x64ut_type\x18\x02 \x01(\x0e\x32*.bigspicy.DesignRegion.DeviceUnderTestType\x12\x16\n\x0e\x66or_top_module\x18\x03 \x01(\t\x12\x11\n\tinstances\x18\x04 \x03(\t\x12#\n\tdc_biases\x18\x05 \x03(\x0b\x32\x10.bigspicy.DCBias\x12\'\n\x05loads\x18\x06 \x03(\x0b\x32\x18.bigspicy.CapacitiveLoad\x12*\n\x07\x64rivers\x18\x07 \x03(\x0b\x32\x19.bigspicy.SimulatedDriver\x12.\n\x0evoltage_probes\x18\x08 \x03(\x0b\x32\x16.bigspicy.VoltageProbe\x12%\n\x05ports\x18\t \x03(\x0b\x32\x16.bigspicy.AnalysisPort\"F\n\x13\x44\x65viceUnderTestType\x12\x0e\n\nSUB_REGION\x10\x00\x12\n\n\x06MODULE\x10\x01\x12\x13\n\x0f\x45XTERNAL_MODULE\x10\x02\"A\n\x0f\x43ircuitAnalysis\x12.\n\x0e\x64\x65sign_regions\x18\x01 \x03(\x0b\x32\x16.bigspicy.DesignRegionb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.circuit_analysis_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NET._serialized_start=42
  _NET._serialized_end=83
  _SIMULATEDDRIVER._serialized_start=85
  _SIMULATEDDRIVER._serialized_end=130
  _CAPACITIVELOAD._serialized_start=132
  _CAPACITIVELOAD._serialized_end=193
  _DCBIAS._serialized_start=195
  _DCBIAS._serialized_end=231
  _VOLTAGEPROBE._serialized_start=233
  _VOLTAGEPROBE._serialized_end=275
  _ANALYSISPORT._serialized_start=277
  _ANALYSISPORT._serialized_end=347
  _DESIGNREGION._serialized_start=350
  _DESIGNREGION._serialized_end=764
  _DESIGNREGION_DEVICEUNDERTESTTYPE._serialized_start=694
  _DESIGNREGION_DEVICEUNDERTESTTYPE._serialized_end=764
  _CIRCUITANALYSIS._serialized_start=766
  _CIRCUITANALYSIS._serialized_end=831
# @@protoc_insertion_point(module_scope)