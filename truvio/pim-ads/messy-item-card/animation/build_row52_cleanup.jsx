// Row 52 Clean-up: builds the After Effects comp from the layer PNGs in ./assets.
// Run in After Effects: File > Scripts > Run Script File, then pick this file.
// Every layer is a full-frame 2160x2160 PNG at 50 percent scale, so it sits exactly where it sits in the .ai.
// Layers in a mask group go into a precomp (Row52_CleanBody, Row52_Assets) with a rectangle mask on it.
// Keyframe eases carry the in and out influence from the timeline, so the motion matches the preview.
(function () {
  var DATA = {
 "comp": "Row52_CleanUp",
 "w": 1080,
 "h": 1080,
 "fps": 30,
 "dur": 10.0,
 "masks": {
  "CleanBody": [
   561.9,
   481.4,
   448,
   407.1
  ],
  "Assets": [
   717.2,
   608.0,
   293.1,
   296.0
  ]
 },
 "layers": [
  {
   "name": "BG",
   "file": "assets/BG.png",
   "group": null,
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {}
  },
  {
   "name": "Logo",
   "file": "assets/Logo.png",
   "group": null,
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {}
  },
  {
   "name": "Headline",
   "file": "assets/Headline.png",
   "group": null,
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {}
  },
  {
   "name": "Label_BC",
   "file": "assets/Label_BC.png",
   "group": null,
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {}
  },
  {
   "name": "Label_PIM",
   "file": "assets/Label_PIM.png",
   "group": null,
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {}
  },
  {
   "name": "CTA",
   "file": "assets/CTA.png",
   "group": null,
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {}
  },
  {
   "name": "Tile_Today",
   "file": "assets/Tile_Today.png",
   "group": null,
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {}
  },
  {
   "name": "Red_L1",
   "file": "assets/Red_L1.png",
   "group": null,
   "anchor": [
    290.3,
    676.4
   ],
   "keys": {
    "s": [
     [
      0.8,
      [
       100,
       100
      ],
      [
       60,
       60
      ]
     ],
     [
      1.2,
      [
       103,
       103
      ],
      [
       60,
       60
      ]
     ],
     [
      1.7,
      [
       100,
       100
      ],
      [
       60,
       60
      ]
     ]
    ]
   }
  },
  {
   "name": "Red_L2",
   "file": "assets/Red_L2.png",
   "group": null,
   "anchor": [
    290.3,
    789.45
   ],
   "keys": {
    "s": [
     [
      0.92,
      [
       100,
       100
      ],
      [
       60,
       60
      ]
     ],
     [
      1.32,
      [
       103,
       103
      ],
      [
       60,
       60
      ]
     ],
     [
      1.82,
      [
       100,
       100
      ],
      [
       60,
       60
      ]
     ]
    ]
   }
  },
  {
   "name": "Red_L3",
   "file": "assets/Red_L3.png",
   "group": null,
   "anchor": [
    290.3,
    902.4
   ],
   "keys": {
    "s": [
     [
      1.04,
      [
       100,
       100
      ],
      [
       60,
       60
      ]
     ],
     [
      1.44,
      [
       103,
       103
      ],
      [
       60,
       60
      ]
     ],
     [
      1.94,
      [
       100,
       100
      ],
      [
       60,
       60
      ]
     ]
    ]
   }
  },
  {
   "name": "Tile_PIM_base",
   "file": "assets/Tile_PIM_base.png",
   "group": null,
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {}
  },
  {
   "name": "Tile_PIM_clutter",
   "file": "assets/Tile_PIM_clutter.png",
   "group": null,
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {}
  },
  {
   "name": "Red_R3",
   "file": "assets/Red_R3.png",
   "group": null,
   "anchor": [
    780.98,
    903.06
   ],
   "keys": {
    "s": [
     [
      1.04,
      [
       100,
       100
      ],
      [
       60,
       60
      ]
     ],
     [
      1.44,
      [
       103,
       103
      ],
      [
       60,
       60
      ]
     ],
     [
      1.94,
      [
       100,
       100
      ],
      [
       60,
       60
      ]
     ]
    ]
   }
  },
  {
   "name": "Clean_body",
   "file": "assets/Clean_body.png",
   "group": "CleanBody",
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {
    "p": [
     [
      3.35,
      [
       0,
       407.1
      ],
      [
       15,
       15
      ]
     ],
     [
      4.45,
      [
       0,
       0
      ],
      [
       85,
       15
      ]
     ]
    ]
   }
  },
  {
   "name": "Clean_title",
   "file": "assets/Clean_title.png",
   "group": "CleanBody",
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {
    "p": [
     [
      3.5,
      [
       0,
       407.1
      ],
      [
       15,
       15
      ]
     ],
     [
      4.65,
      [
       0,
       0
      ],
      [
       85,
       15
      ]
     ]
    ]
   }
  },
  {
   "name": "Clean_tab",
   "file": "assets/Clean_tab.png",
   "group": "CleanBody",
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {
    "p": [
     [
      3.6,
      [
       0,
       407.1
      ],
      [
       15,
       15
      ]
     ],
     [
      4.75,
      [
       0,
       0
      ],
      [
       85,
       15
      ]
     ]
    ]
   }
  },
  {
   "name": "Clean_no",
   "file": "assets/Clean_no.png",
   "group": "CleanBody",
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {
    "p": [
     [
      3.7,
      [
       0,
       407.1
      ],
      [
       15,
       15
      ]
     ],
     [
      4.85,
      [
       0,
       0
      ],
      [
       85,
       15
      ]
     ]
    ]
   }
  },
  {
   "name": "Clean_desc",
   "file": "assets/Clean_desc.png",
   "group": "CleanBody",
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {
    "p": [
     [
      3.8,
      [
       0,
       407.1
      ],
      [
       15,
       15
      ]
     ],
     [
      4.95,
      [
       0,
       0
      ],
      [
       85,
       15
      ]
     ]
    ]
   }
  },
  {
   "name": "Clean_cat",
   "file": "assets/Clean_cat.png",
   "group": "CleanBody",
   "anchor": [
    540.0,
    540.0
   ],
   "keys": {
    "p": [
     [
      3.9,
      [
       0,
       407.1
      ],
      [
       15,
       15
      ]
     ],
     [
      5.05,
      [
       0,
       0
      ],
      [
       85,
       15
      ]
     ]
    ]
   }
  },
  {
   "name": "Red_R1",
   "file": "assets/Red_R1.png",
   "group": null,
   "anchor": [
    780.98,
    676.15
   ],
   "keys": {
    "s": [
     [
      0.8,
      [
       100,
       100
      ],
      [
       60,
       60
      ]
     ],
     [
      1.2,
      [
       103,
       103
      ],
      [
       60,
       60
      ]
     ],
     [
      1.7,
      [
       100,
       100
      ],
      [
       60,
       60
      ]
     ],
     [
      2.6,
      [
       100,
       100
      ],
      [
       60,
       60
      ]
     ],
     [
      3.8,
      [
       58,
       58
      ],
      [
       60,
       60
      ]
     ]
    ],
    "p": [
     [
      2.6,
      [
       0,
       0
      ],
      [
       60,
       60
      ]
     ],
     [
      3.8,
      [
       100.36,
       76.09
      ],
      [
       60,
       60
      ]
     ]
    ]
   }
  },
  {
   "name": "Red_R2",
   "file": "assets/Red_R2.png",
   "group": null,
   "anchor": [
    780.98,
    789.65
   ],
   "keys": {
    "s": [
     [
      0.92,
      [
       100,
       100
      ],
      [
       60,
       60
      ]
     ],
     [
      1.32,
      [
       103,
       103
      ],
      [
       60,
       60
      ]
     ],
     [
      1.82,
      [
       100,
       100
      ],
      [
       60,
       60
      ]
     ],
     [
      2.8,
      [
       100,
       100
      ],
      [
       60,
       60
      ]
     ],
     [
      4.0,
      [
       58,
       58
      ],
      [
       60,
       60
      ]
     ]
    ],
    "p": [
     [
      2.8,
      [
       0,
       0
      ],
      [
       60,
       60
      ]
     ],
     [
      4.0,
      [
       100.36,
       19.06
      ],
      [
       60,
       60
      ]
     ]
    ]
   }
  },
  {
   "name": "PIM_popup",
   "file": "assets/PIM_popup.png",
   "group": null,
   "anchor": [
    863.75,
    670.35
   ],
   "keys": {
    "o": [
     [
      1.9,
      0,
      [
       15,
       15
      ]
     ],
     [
      2.25,
      100,
      [
       85,
       15
      ]
     ]
    ],
    "s": [
     [
      1.9,
      [
       96,
       96
      ],
      [
       15,
       15
      ]
     ],
     [
      2.85,
      [
       100,
       100
      ],
      [
       85,
       15
      ]
     ]
    ],
    "p": [
     [
      1.9,
      [
       0,
       16
      ],
      [
       15,
       15
      ]
     ],
     [
      2.85,
      [
       0,
       0
      ],
      [
       85,
       15
      ]
     ]
    ]
   }
  },
  {
   "name": "Row1",
   "file": "assets/Row1.png",
   "group": "Assets",
   "anchor": [
    863.75,
    639.15
   ],
   "keys": {
    "p": [
     [
      3.55,
      [
       0,
       288.7
      ],
      [
       15,
       15
      ]
     ],
     [
      4.55,
      [
       0,
       0
      ],
      [
       85,
       15
      ]
     ]
    ]
   }
  },
  {
   "name": "Row2",
   "file": "assets/Row2.png",
   "group": "Assets",
   "anchor": [
    863.75,
    695.62
   ],
   "keys": {
    "p": [
     [
      3.72,
      [
       0,
       232.23
      ],
      [
       15,
       15
      ]
     ],
     [
      4.72,
      [
       0,
       0
      ],
      [
       85,
       15
      ]
     ]
    ]
   }
  },
  {
   "name": "Row3",
   "file": "assets/Row3.png",
   "group": "Assets",
   "anchor": [
    863.75,
    752.09
   ],
   "keys": {
    "p": [
     [
      3.89,
      [
       0,
       175.76
      ],
      [
       15,
       15
      ]
     ],
     [
      4.89,
      [
       0,
       0
      ],
      [
       85,
       15
      ]
     ]
    ]
   }
  },
  {
   "name": "Row4",
   "file": "assets/Row4.png",
   "group": "Assets",
   "anchor": [
    863.75,
    808.56
   ],
   "keys": {
    "p": [
     [
      4.06,
      [
       0,
       119.29
      ],
      [
       15,
       15
      ]
     ],
     [
      5.06,
      [
       0,
       0
      ],
      [
       85,
       15
      ]
     ]
    ]
   }
  },
  {
   "name": "Row5",
   "file": "assets/Row5.png",
   "group": "Assets",
   "anchor": [
    863.75,
    865.03
   ],
   "keys": {
    "p": [
     [
      4.23,
      [
       0,
       62.82
      ],
      [
       15,
       15
      ]
     ],
     [
      5.23,
      [
       0,
       0
      ],
      [
       85,
       15
      ]
     ]
    ]
   }
  }
 ]
};
  var root = new File($.fileName).parent;
  app.beginUndoGroup("Build Row52 Clean-up");
  var folder = app.project.items.addFolder("Row52 assets");
  var main = app.project.items.addComp(DATA.comp, DATA.w, DATA.h, 1, DATA.dur, DATA.fps);
  main.bgColor = [1, 1, 1];
  var pre = {};

  function dimsOf(prop) {
    var t = prop.propertyValueType;
    if (t == PropertyValueType.TwoD_SPATIAL || t == PropertyValueType.ThreeD_SPATIAL || t == PropertyValueType.OneD) return 1;
    if (t == PropertyValueType.TwoD) return 2;
    if (t == PropertyValueType.ThreeD) return 3;
    return 1;
  }
  function keyAll(prop, keys, toValue) {
    var j, d, n = dimsOf(prop);
    for (j = 0; j < keys.length; j++) prop.setValueAtTime(keys[j][0], toValue(keys[j][1]));
    for (j = 0; j < keys.length; j++) {
      var k = prop.nearestKeyIndex(keys[j][0]), ein = [], eout = [];
      for (d = 0; d < n; d++) { ein.push(new KeyframeEase(0, keys[j][2][0])); eout.push(new KeyframeEase(0, keys[j][2][1])); }
      prop.setTemporalEaseAtKey(k, ein, eout);
    }
  }
  function maskLayer(layer, r) {
    var m = layer.property("ADBE Mask Parade").addProperty("ADBE Mask Atom");
    var s = new Shape();
    s.vertices = [[r[0], r[1]], [r[0] + r[2], r[1]], [r[0] + r[2], r[1] + r[3]], [r[0], r[1] + r[3]]];
    s.closed = true;
    m.property("ADBE Mask Shape").setValue(s);
  }
  function target(L) {
    if (!L.group) return main;
    if (!pre[L.group]) {
      var c = app.project.items.addComp("Row52_" + L.group, DATA.w, DATA.h, 1, DATA.dur, DATA.fps);
      c.parentFolder = folder;
      var holder = main.layers.add(c);
      holder.name = L.group + " (masked)";
      maskLayer(holder, DATA.masks[L.group]);
      pre[L.group] = c;
    }
    return pre[L.group];
  }

  for (var i = 0; i < DATA.layers.length; i++) {
    var L = DATA.layers[i];
    var item = app.project.importFile(new ImportOptions(new File(root.fsName + "/" + L.file)));
    item.parentFolder = folder;
    var layer = target(L).layers.add(item);
    layer.name = L.name;
    var tr = layer.property("ADBE Transform Group");
    var ap = tr.property("ADBE Anchor Point"), pos = tr.property("ADBE Position");
    var sc = tr.property("ADBE Scale"), op = tr.property("ADBE Opacity");
    var ax = L.anchor[0], ay = L.anchor[1];
    ap.setValue([ax * 2, ay * 2]);
    pos.setValue([ax, ay]);
    sc.setValue([50, 50]);
    if (L.keys.o) keyAll(op, L.keys.o, function (v) { return v; });
    if (L.keys.p) keyAll(pos, L.keys.p, function (v) { return [ax + v[0], ay + v[1]]; });
    if (L.keys.s) keyAll(sc, L.keys.s, function (v) { return [v[0] / 2, v[1] / 2]; });
    layer.motionBlur = !!(L.keys.p || L.keys.s);
  }
  main.motionBlur = true;
  for (var g in pre) pre[g].motionBlur = true;
  main.openInViewer();
  app.endUndoGroup();
})();
