// Row 52 Clean-up: builds the After Effects comp from the layer PNGs in ./assets.
// Run in After Effects: File > Scripts > Run Script File, then pick this file.
// Every layer is a full-frame 2160x2160 PNG at 50 percent scale, so it sits exactly where it sits in the .ai.
// Anchor points sit on each moving part, so scale happens around the part. Keyframes use 60 percent ease.
(function () {
  var DATA = {
 "comp": "Row52_CleanUp",
 "w": 1080,
 "h": 1080,
 "fps": 30,
 "dur": 6.0,
 "layers": [
  {
   "name": "BG",
   "file": "assets/BG.png",
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {}
  },
  {
   "name": "Logo",
   "file": "assets/Logo.png",
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {}
  },
  {
   "name": "Headline",
   "file": "assets/Headline.png",
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {}
  },
  {
   "name": "Label_BC",
   "file": "assets/Label_BC.png",
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {}
  },
  {
   "name": "Label_PIM",
   "file": "assets/Label_PIM.png",
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {}
  },
  {
   "name": "CTA",
   "file": "assets/CTA.png",
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {}
  },
  {
   "name": "Tile_Today",
   "file": "assets/Tile_Today.png",
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {}
  },
  {
   "name": "Red_L1",
   "file": "assets/Red_L1.png",
   "anchor": [
    290.3,
    676.4
   ],
   "keys": {
    "s": [
     [
      0.6,
      [
       100,
       100
      ]
     ],
     [
      0.85,
      [
       104,
       104
      ]
     ],
     [
      1.15,
      [
       100,
       100
      ]
     ]
    ]
   }
  },
  {
   "name": "Red_L2",
   "file": "assets/Red_L2.png",
   "anchor": [
    290.3,
    789.45
   ],
   "keys": {
    "s": [
     [
      0.68,
      [
       100,
       100
      ]
     ],
     [
      0.93,
      [
       104,
       104
      ]
     ],
     [
      1.23,
      [
       100,
       100
      ]
     ]
    ]
   }
  },
  {
   "name": "Red_L3",
   "file": "assets/Red_L3.png",
   "anchor": [
    290.3,
    902.4
   ],
   "keys": {
    "s": [
     [
      0.76,
      [
       100,
       100
      ]
     ],
     [
      1.01,
      [
       104,
       104
      ]
     ],
     [
      1.31,
      [
       100,
       100
      ]
     ]
    ]
   }
  },
  {
   "name": "Tile_PIM_clean",
   "file": "assets/Tile_PIM_clean.png",
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {}
  },
  {
   "name": "Tile_PIM_clutter",
   "file": "assets/Tile_PIM_clutter.png",
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {
    "o": [
     [
      2.4,
      100
     ],
     [
      3.0,
      0
     ]
    ]
   }
  },
  {
   "name": "Red_R3",
   "file": "assets/Red_R3.png",
   "anchor": [
    780.98,
    903.06
   ],
   "keys": {
    "s": [
     [
      0.76,
      [
       100,
       100
      ]
     ],
     [
      1.01,
      [
       104,
       104
      ]
     ],
     [
      1.31,
      [
       100,
       100
      ]
     ]
    ],
    "o": [
     [
      2.4,
      100
     ],
     [
      3.0,
      0
     ]
    ]
   }
  },
  {
   "name": "PIM_popup",
   "file": "assets/PIM_popup.png",
   "anchor": [
    863.75,
    670.35
   ],
   "keys": {
    "o": [
     [
      1.15,
      0
     ],
     [
      1.45,
      100
     ]
    ],
    "s": [
     [
      1.15,
      [
       88,
       88
      ]
     ],
     [
      1.5,
      [
       102,
       102
      ]
     ],
     [
      1.7,
      [
       100,
       100
      ]
     ]
    ],
    "p": [
     [
      1.15,
      [
       0,
       20
      ]
     ],
     [
      1.5,
      [
       0,
       0
      ]
     ]
    ]
   }
  },
  {
   "name": "Row1",
   "file": "assets/Row1.png",
   "anchor": [
    863.75,
    639.15
   ],
   "keys": {
    "o": [
     [
      2.3,
      0
     ],
     [
      2.55,
      100
     ]
    ],
    "s": [
     [
      2.3,
      [
       96,
       96
      ]
     ],
     [
      2.55,
      [
       100,
       100
      ]
     ]
    ]
   }
  },
  {
   "name": "Row2",
   "file": "assets/Row2.png",
   "anchor": [
    863.75,
    695.62
   ],
   "keys": {
    "o": [
     [
      2.5,
      0
     ],
     [
      2.75,
      100
     ]
    ],
    "s": [
     [
      2.5,
      [
       96,
       96
      ]
     ],
     [
      2.75,
      [
       100,
       100
      ]
     ]
    ]
   }
  },
  {
   "name": "Row3",
   "file": "assets/Row3.png",
   "anchor": [
    863.75,
    752.09
   ],
   "keys": {
    "o": [
     [
      2.75,
      0
     ],
     [
      3.05,
      100
     ]
    ],
    "p": [
     [
      2.75,
      [
       0,
       14
      ]
     ],
     [
      3.05,
      [
       0,
       0
      ]
     ]
    ]
   }
  },
  {
   "name": "Row4",
   "file": "assets/Row4.png",
   "anchor": [
    863.75,
    808.56
   ],
   "keys": {
    "o": [
     [
      2.9,
      0
     ],
     [
      3.2,
      100
     ]
    ],
    "p": [
     [
      2.9,
      [
       0,
       14
      ]
     ],
     [
      3.2,
      [
       0,
       0
      ]
     ]
    ]
   }
  },
  {
   "name": "Row5",
   "file": "assets/Row5.png",
   "anchor": [
    863.75,
    865.03
   ],
   "keys": {
    "o": [
     [
      3.05,
      0
     ],
     [
      3.35,
      100
     ]
    ],
    "p": [
     [
      3.05,
      [
       0,
       14
      ]
     ],
     [
      3.35,
      [
       0,
       0
      ]
     ]
    ]
   }
  },
  {
   "name": "Red_R1",
   "file": "assets/Red_R1.png",
   "anchor": [
    780.98,
    676.15
   ],
   "keys": {
    "s": [
     [
      0.6,
      [
       100,
       100
      ]
     ],
     [
      0.85,
      [
       104,
       104
      ]
     ],
     [
      1.15,
      [
       100,
       100
      ]
     ],
     [
      1.32,
      [
       100,
       100
      ]
     ],
     [
      1.55,
      [
       103,
       103
      ]
     ],
     [
      1.75,
      [
       103,
       103
      ]
     ],
     [
      2.5,
      [
       61.73,
       81.63
      ]
     ]
    ],
    "p": [
     [
      1.75,
      [
       0,
       0
      ]
     ],
     [
      2.5,
      [
       82.77,
       -37.0
      ]
     ]
    ],
    "o": [
     [
      2.3,
      100
     ],
     [
      2.5,
      0
     ]
    ]
   }
  },
  {
   "name": "Red_R2",
   "file": "assets/Red_R2.png",
   "anchor": [
    780.98,
    789.65
   ],
   "keys": {
    "s": [
     [
      0.68,
      [
       100,
       100
      ]
     ],
     [
      0.93,
      [
       104,
       104
      ]
     ],
     [
      1.23,
      [
       100,
       100
      ]
     ],
     [
      1.32,
      [
       100,
       100
      ]
     ],
     [
      1.55,
      [
       103,
       103
      ]
     ],
     [
      1.95,
      [
       103,
       103
      ]
     ],
     [
      2.7,
      [
       61.73,
       100.02
      ]
     ]
    ],
    "p": [
     [
      1.95,
      [
       0,
       0
      ]
     ],
     [
      2.7,
      [
       82.77,
       -94.03
      ]
     ]
    ],
    "o": [
     [
      2.5,
      100
     ],
     [
      2.7,
      0
     ]
    ]
   }
  }
 ]
};
  var root = new File($.fileName).parent;
  app.beginUndoGroup("Build Row52 Clean-up");
  var folder = app.project.items.addFolder("Row52 assets");
  var comp = app.project.items.addComp(DATA.comp, DATA.w, DATA.h, 1, DATA.dur, DATA.fps);
  comp.bgColor = [1, 1, 1];
  function ease(prop) {
    for (var k = 1; k <= prop.numKeys; k++) {
      var dims = 1;
      if (prop.propertyValueType == PropertyValueType.TwoD) dims = 2;
      if (prop.propertyValueType == PropertyValueType.ThreeD) dims = 3;
      if (prop.propertyValueType == PropertyValueType.TwoD_SPATIAL || prop.propertyValueType == PropertyValueType.ThreeD_SPATIAL) dims = 1;
      var e = [];
      for (var d = 0; d < dims; d++) e.push(new KeyframeEase(0, 60));
      prop.setTemporalEaseAtKey(k, e, e);
    }
  }
  for (var i = 0; i < DATA.layers.length; i++) {
    var L = DATA.layers[i];
    var item = app.project.importFile(new ImportOptions(new File(root.fsName + "/" + L.file)));
    item.parentFolder = folder;
    var layer = comp.layers.add(item);
    layer.name = L.name;
    var tr = layer.property("ADBE Transform Group");
    var ap = tr.property("ADBE Anchor Point"), pos = tr.property("ADBE Position");
    var sc = tr.property("ADBE Scale"), op = tr.property("ADBE Opacity");
    ap.setValue([L.anchor[0] * 2, L.anchor[1] * 2]);
    pos.setValue([L.anchor[0], L.anchor[1]]);
    sc.setValue([50, 50]);
    var keys = L.keys, j;
    if (keys.o) { for (j = 0; j < keys.o.length; j++) op.setValueAtTime(keys.o[j][0], keys.o[j][1]); ease(op); }
    if (keys.p) {
      for (j = 0; j < keys.p.length; j++) pos.setValueAtTime(keys.p[j][0], [L.anchor[0] + keys.p[j][1][0], L.anchor[1] + keys.p[j][1][1]]);
      ease(pos);
    }
    if (keys.s) {
      for (j = 0; j < keys.s.length; j++) sc.setValueAtTime(keys.s[j][0], [keys.s[j][1][0] / 2, keys.s[j][1][1] / 2]);
      ease(sc);
    }
  }
  comp.openInViewer();
  app.endUndoGroup();
})();
