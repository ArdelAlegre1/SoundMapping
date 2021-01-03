import numpy as np

EIGEN_VALUES_0101 = np.array([5.61242810e-01, 2.97843608e-01, 2.87688759e-02, 6.95740460e-03,
       1.14006552e-03, 5.85919805e-04, 4.58054614e-04, 3.57030764e-04,
       2.50261374e-04, 2.17791640e-05, 3.82897966e-05, 4.81229024e-05,
       6.56781483e-05, 1.25972958e-04, 1.07175368e-04, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00])

EIGEN_VECTORS_0101 = np.array([[-0.43349642,  0.27495556,  0.39057389, -0.03742823, -0.31376425,
        -0.20572038,  0.10528668, -0.1673914 ,  0.0486316 ,  0.27542519,
        -0.22545765, -0.1725862 ,  0.4513455 , -0.19962015,  0.01597643,
         0.        ,  0.        ,  0.        ],
       [ 0.16453434,  0.16959243,  0.08605369, -0.19733673, -0.19904958,
        -0.17737256,  0.48854573,  0.11654601, -0.17352328,  0.24203459,
        -0.08421957,  0.03779132, -0.21026199,  0.59317694, -0.28495085,
         0.        ,  0.        ,  0.        ],
       [ 0.04669912,  0.2382891 , -0.22393179,  0.14633468,  0.00750594,
        -0.36789529,  0.43997229, -0.18132541,  0.19780151, -0.56970191,
         0.2693233 ,  0.07297427,  0.23662152, -0.06366522, -0.0776622 ,
         0.        ,  0.        ,  0.        ],
       [ 0.23482871,  0.4071538 , -0.33535639, -0.54625097, -0.12507093,
         0.23350896, -0.15383027, -0.39800375, -0.15526823, -0.00774004,
        -0.00118549, -0.06171634,  0.14161181,  0.05249045,  0.25534235,
         0.        ,  0.        ,  0.        ],
       [ 0.25275671,  0.01347188,  0.16304144,  0.45311601, -0.3170313 ,
         0.05222677,  0.1980313 , -0.02643876, -0.23162449, -0.04281618,
        -0.03167388, -0.04096205, -0.10395404,  0.05144629,  0.69947596,
         0.        ,  0.        ,  0.        ],
       [ 0.23085157, -0.06030014, -0.2562761 ,  0.26156236, -0.73090441,
        -0.02364891, -0.3189801 , -0.0153632 ,  0.06025349,  0.03822491,
         0.03232575,  0.02335293,  0.02271851, -0.08666717, -0.396869  ,
         0.        ,  0.        ,  0.        ],
       [-0.44678142,  0.23641118,  0.05774433,  0.01603282, -0.14629699,
         0.00838209, -0.06460261, -0.32994134,  0.03547098, -0.21431866,
        -0.07250177,  0.07674632, -0.73634247, -0.06927257, -0.03256836,
         0.        ,  0.        ,  0.        ],
       [ 0.17045321,  0.36167394, -0.21008484,  0.01941763,  0.11132556,
        -0.17533198,  0.18104008,  0.26549275, -0.11144264,  0.42426641,
         0.10248602,  0.14782006, -0.22861378, -0.61006298,  0.00341799,
         0.        ,  0.        ,  0.        ],
       [-0.11777081, -0.0969376 , -0.30937632,  0.31275835,  0.169178  ,
        -0.05840825,  0.0305045 , -0.48139556,  0.28447618,  0.5275285 ,
         0.09800825,  0.27018398,  0.0520648 ,  0.2512371 ,  0.10415313,
         0.        ,  0.        ,  0.        ],
       [-0.34142032,  0.20273907, -0.42697937, -0.00470684, -0.12033666,
        -0.03842418, -0.08383152,  0.53742876,  0.35509838,  0.01260448,
        -0.02302155, -0.2627332 , -0.0200493 ,  0.25530995,  0.29458984,
         0.        ,  0.        ,  0.        ],
       [ 0.17661495,  0.4921134 ,  0.30451617,  0.19827208,  0.06452658,
         0.52260547, -0.02250354,  0.13309117,  0.40484938, -0.04710477,
        -0.05265429,  0.31962803,  0.08337833,  0.08534421, -0.11746406,
         0.        ,  0.        ,  0.        ],
       [ 0.11862906,  0.10262623, -0.05002856,  0.26268533,  0.17651281,
         0.27129722,  0.17136159, -0.19295772,  0.04600637,  0.10049353,
         0.06768967, -0.80552018, -0.10085493, -0.04514531, -0.23379932,
         0.        ,  0.        ,  0.        ],
       [ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
         0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
         0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
         1.        ,  0.        ,  0.        ],
       [ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
         0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
         0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
         0.        ,  1.        ,  0.        ],
       [ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
         0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
         0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
         0.        ,  0.        ,  1.        ],
       [-0.4007572 ,  0.16247284, -0.25811037,  0.29916065,  0.06919308,
         0.30858482,  0.03695538,  0.09417975, -0.65331281, -0.0632964 ,
         0.05209488,  0.15585533,  0.22261041,  0.09609581, -0.17323905,
         0.        ,  0.        ,  0.        ],
       [ 0.20971576,  0.33699439,  0.01293722,  0.26424074,  0.30739939,
        -0.47420343, -0.4528482 , -0.03274771, -0.15137633, -0.07888687,
        -0.41867234, -0.07379534,  0.00927034,  0.18692851, -0.04536446,
         0.        ,  0.        ,  0.        ],
       [ 0.03933328, -0.19848336, -0.31250771,  0.00383268,  0.00112526,
         0.1747746 ,  0.33289348, -0.03699985,  0.10275872, -0.10353083,
        -0.81008704,  0.0830546 ,  0.01920169, -0.18041423, -0.03622085,
         0.        ,  0.        ,  0.        ]])

EIGEN_VALUES_0819 = np.array([0.51015896, 0.4791336 , 0.11420783, 0.06683177, 0.05302011,
       0.03465207, 0.02601994, 0.01749594, 0.01317495, 0.01170303,
       0.0102567 , 0.00859016, 0.00761653, 0.00164344, 0.00231119,
       0.00324752, 0.00412781, 0.00558874])

EIGEN_VECTORS_0819 = np.array([[ 1.34168638e-01, -1.72949087e-01, -1.52193738e-01,
         3.82161039e-01,  7.31262556e-01,  2.35391567e-01,
        -4.23529527e-02, -1.17175501e-02,  1.52573316e-01,
         1.02313779e-01,  1.92462576e-01, -2.92485557e-01,
         1.76074105e-01, -8.80435017e-04,  3.07549495e-02,
         2.61056334e-02, -4.09791232e-02,  1.20959268e-02],
       [-4.99667619e-02,  1.75309538e-01,  5.29465965e-01,
         1.43779043e-01,  2.90413485e-01,  1.94472773e-01,
        -8.80812498e-02,  2.06833301e-01, -2.05819688e-01,
        -2.25306117e-02, -4.42768090e-01,  1.07333686e-01,
        -1.76716290e-01, -3.27290190e-02,  5.35346689e-02,
        -1.68081203e-01,  1.98263888e-01, -3.74040324e-01],
       [-2.80248517e-02,  1.06655977e-01,  3.19391582e-01,
        -7.90114596e-03,  6.07187010e-02,  1.20119163e-01,
         1.58012342e-01,  2.16243110e-01, -2.31030456e-01,
         6.43716448e-02, -8.90771205e-02,  2.90257004e-04,
         9.87960027e-02,  1.31331369e-01,  5.59374635e-02,
         1.28608707e-01, -6.95849421e-01,  4.46747748e-01],
       [-2.88411516e-01,  3.74560045e-01,  9.97000375e-02,
        -1.68120514e-01,  8.12677873e-02, -9.34937950e-02,
         1.73405431e-01,  5.42960693e-01,  1.10892809e-01,
        -2.38112408e-01,  4.20887611e-01, -2.21848956e-01,
         1.90540796e-01,  7.65812291e-02, -1.34824517e-01,
         7.30756369e-03,  1.97158207e-01, -5.88786954e-02],
       [ 4.85155833e-01,  3.05436002e-01,  2.53834376e-01,
        -1.12219317e-02, -1.74835129e-02, -3.61710388e-02,
         1.84794590e-01, -2.42976388e-01, -2.54438364e-01,
         3.47881096e-01,  5.04990430e-01,  9.51147811e-02,
        -3.18370065e-02,  2.17599771e-03, -5.51211291e-02,
         3.73981610e-02,  1.51559476e-04, -2.38110592e-01],
       [ 1.29663086e-02,  1.30887148e-01, -9.84307515e-03,
         4.17846085e-02, -2.15439713e-01, -1.48729232e-02,
        -5.90280402e-02,  3.82459253e-02,  7.19105891e-02,
         8.88628594e-02,  2.97728185e-02, -2.41314022e-01,
         2.89900370e-01, -2.93731515e-01,  6.87768088e-01,
        -4.17601210e-01, -1.48512130e-01, -1.31515941e-01],
       [-2.06988064e-01,  3.01917392e-01, -3.51815420e-01,
        -1.33753174e-02,  3.47796257e-01, -5.43433779e-01,
        -1.40375412e-01,  8.82234710e-02, -7.67437603e-02,
         2.49001974e-01, -8.87782769e-02,  3.45324717e-01,
        -4.32669695e-02, -1.22093469e-01,  7.62726828e-02,
         1.03256216e-01, -2.16351616e-01, -1.52279771e-01],
       [ 2.91692758e-01,  1.15796240e-01, -2.23638963e-01,
         1.97092484e-01, -1.59139290e-01, -6.28813786e-02,
        -5.47087169e-01,  3.00749422e-01, -3.81921101e-01,
        -5.36990065e-02,  3.76992297e-02, -2.31023343e-01,
        -1.61997649e-01,  3.67777443e-01,  8.64169215e-02,
         2.23945716e-02,  9.11768077e-02,  1.10843769e-01],
       [-1.53283978e-01,  5.81719907e-02, -6.16716156e-02,
         1.59404263e-02, -2.16343860e-02,  1.44142248e-02,
         1.99981520e-01, -2.06650177e-01,  6.69917863e-02,
         9.54053797e-02, -1.49688144e-01,  5.44078186e-02,
         3.14675420e-01,  7.96379350e-01,  2.21804866e-01,
         5.57024638e-02,  4.06089380e-02, -2.44014468e-01],
       [ 1.37592667e-01, -2.37441091e-02, -5.29475160e-02,
        -7.67062348e-01,  2.45643431e-01,  2.91428340e-01,
        -3.33962048e-01,  2.82305405e-02, -2.91605325e-02,
         1.54282335e-01, -1.68771393e-02,  1.43174229e-01,
         2.22972172e-01,  4.37007429e-02,  2.42900413e-02,
        -1.22968463e-01,  9.13205531e-02,  1.02973271e-01],
       [ 1.98560095e-01,  6.39532873e-02, -4.36555833e-01,
        -7.24409148e-02, -4.98766070e-02,  2.92982447e-01,
         5.17375031e-01,  3.86717555e-01,  4.26627784e-02,
         2.90018722e-01, -1.89008167e-01, -1.12484930e-02,
        -3.44040496e-01,  9.25975716e-03,  5.95988659e-02,
        -9.09486832e-02,  5.20105143e-02, -1.84778159e-02],
       [ 9.33302286e-02,  3.96814005e-02, -1.12468562e-01,
        -3.14477509e-01,  4.33445375e-02, -1.89209890e-02,
         5.22561928e-04, -1.52944498e-01, -3.66549623e-02,
        -2.76260727e-01, -1.42908453e-01, -5.07088270e-01,
        -1.64368300e-01, -1.79034116e-02, -1.45142878e-01,
         1.36277509e-01, -4.23023936e-01, -5.01388950e-01],
       [-2.54355585e-01,  4.14974044e-01,  7.40231937e-02,
         7.29790987e-02, -1.61939866e-01,  1.95723879e-01,
        -2.90734759e-01, -1.59516514e-01,  3.83385914e-01,
         5.02081497e-01, -9.24464093e-02, -2.85193085e-01,
        -1.35496723e-01,  8.50974900e-03, -2.40049219e-01,
         4.15591564e-02, -2.11946842e-02,  1.02985511e-01],
       [ 4.00118495e-01,  3.76553170e-01,  6.37567513e-02,
        -8.03947548e-02,  1.80724112e-01, -3.25165826e-01,
         1.82852881e-01, -1.98503940e-01,  1.71164068e-01,
        -2.07687354e-01, -3.63829177e-01, -2.00283149e-01,
         5.75862195e-02, -1.65865763e-02,  8.35001847e-02,
         4.54166130e-02,  2.54027673e-01,  3.92783873e-01],
       [ 1.04596212e-01,  1.62330055e-02, -1.22649729e-01,
         1.27418337e-01, -4.79304836e-02, -1.28418864e-01,
         5.12765752e-02,  1.56975500e-02, -1.18098425e-01,
         3.78310033e-02, -1.52663433e-01, -6.38635254e-03,
         3.43504665e-01,  4.71162556e-02, -5.72123982e-01,
        -6.57932332e-01, -1.28106024e-01, -1.73381317e-02],
       [-2.75639480e-01,  4.31107738e-01, -3.11576280e-01,
         8.60467463e-02,  5.79270698e-02,  4.22621751e-01,
         6.39679337e-02, -3.70843973e-01, -3.84679740e-01,
        -3.29593405e-01,  7.56047391e-02,  1.02152230e-01,
        -1.87394966e-02, -1.09146034e-01,  3.21175260e-02,
        -7.52018765e-02,  4.55120962e-02,  1.27748312e-01],
       [ 3.44018250e-01,  2.27697684e-01, -1.07129440e-01,
         1.89287215e-01, -1.87741974e-01,  2.68685516e-01,
        -1.50776112e-01,  1.87914395e-01,  3.18851944e-01,
        -2.18323355e-01, -1.15341285e-01,  3.53328088e-01,
         3.68368213e-01, -1.29331225e-01, -9.79022530e-02,
         3.25194635e-01, -1.39302201e-01, -2.05852909e-01],
       [-1.06960227e-01, -1.05485558e-01, -5.70413650e-02,
         4.05425722e-03, -1.12496924e-01, -1.13792792e-02,
         1.10229989e-01,  4.90392964e-02, -4.45699307e-01,
         2.96808993e-01, -2.33552519e-01, -2.76270268e-01,
         4.56833033e-01, -2.67623670e-01, -9.26757998e-02,
         4.17590661e-01,  2.53470918e-01, -4.08533207e-02]])

EIGEN_VALUES = np.array([0.11643512, 0.06973232, 0.06414829, 0.05811179, 0.05008431,
       0.04354229, 0.01247356, 0.03666576, 0.03193203, 0.01598887,
       0.0179332 , 0.02827345, 0.02493487, 0.0216032 , 0.02269648,
       0.        , 0.        , 0.        ])

EIGEN_VECTORS = np.array([[-5.58767736e-02,  1.62917742e-01, -6.14916360e-02,
         5.95497004e-02,  1.30366390e-01,  3.07711513e-02,
         9.49480861e-01,  2.61951998e-02, -4.72443414e-02,
        -1.42676820e-01,  5.26842567e-02, -8.62183737e-02,
         5.18067375e-02,  8.51525395e-02,  1.15333635e-02,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
       [ 4.30837996e-01, -3.62281942e-01,  7.21579731e-02,
        -3.53786592e-01, -4.22010358e-01, -4.39277553e-03,
         1.57999909e-01,  1.25305142e-01,  1.08400426e-01,
        -1.92185899e-01, -4.64822554e-01,  1.20128015e-02,
        -8.57618923e-02,  2.26602033e-01, -1.01918261e-01,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
       [-2.86914334e-01,  3.09984945e-01, -5.37820740e-02,
         2.70209975e-01,  2.50976716e-01,  3.14470554e-02,
        -1.40307424e-01,  7.03901168e-02,  3.78869520e-02,
        -2.82347894e-01, -6.82458904e-01,  1.25748812e-01,
        -2.10032252e-02,  2.68376824e-01, -1.47913681e-01,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
       [ 5.54444980e-01,  5.88946925e-01,  4.55093269e-02,
        -3.10815308e-01,  2.34255150e-01, -3.60533478e-01,
        -6.71614168e-02, -1.08734028e-01, -1.47298100e-01,
        -4.08721680e-02, -1.83379942e-02,  1.13682340e-01,
         6.48345454e-02, -3.06457578e-02,  6.39649893e-02,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
       [ 1.97902535e-02, -1.68688169e-01,  7.29422375e-02,
         3.27976112e-02,  4.63613525e-02,  9.97833675e-03,
        -2.16462066e-02, -6.58927757e-01, -8.95549073e-02,
         6.84066726e-02,  9.21833315e-02,  5.17326594e-02,
         4.05730828e-01,  5.66673781e-01, -1.35066046e-01,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
       [ 2.18059627e-01,  1.67952396e-01,  8.13722644e-01,
         4.46085221e-01, -1.63697035e-01,  1.66230004e-01,
         2.42896742e-02,  3.49515403e-02,  3.60206030e-02,
         5.54603172e-03,  3.76710791e-02, -4.22035194e-02,
        -4.79862759e-02, -4.15934668e-04, -5.77483992e-03,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
       [ 2.27959317e-01,  2.83660227e-02, -1.28379104e-01,
         6.53117002e-02,  2.67956772e-01,  6.55826408e-02,
        -5.92075055e-03, -1.08698326e-01,  5.21207950e-01,
         8.03597713e-02,  1.87318824e-01, -1.56511796e-01,
        -4.56064259e-01,  1.20826410e-01, -5.27482205e-01,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
       [ 1.89267236e-01, -4.65449522e-01,  5.84480809e-02,
         3.09636752e-01,  4.55767679e-01, -5.04994331e-01,
         9.82100564e-04,  1.11954763e-01,  5.08707115e-02,
        -1.56138553e-02, -1.03748576e-01, -2.48091027e-01,
         1.39660435e-02,  4.43809137e-02,  3.09283060e-01,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
       [ 2.55596418e-02,  1.06800135e-01, -9.20649936e-02,
        -1.95643097e-02, -4.68161562e-02,  2.11460534e-01,
        -8.77104484e-02, -9.95854753e-02,  2.87734954e-01,
        -3.68107619e-01,  2.17149760e-01,  7.97823585e-02,
        -2.87396609e-01,  3.37174341e-01,  6.68181710e-01,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
       [ 4.42586641e-01, -3.41341534e-02, -3.69514323e-01,
         3.41468327e-01,  4.69219386e-02,  4.26231564e-01,
        -8.92977980e-02,  1.86702177e-01, -5.31417818e-01,
        -3.55086106e-03,  5.54237197e-02, -1.13237233e-01,
        -4.55402045e-02,  1.45697047e-01, -3.86024891e-02,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
       [ 1.15756378e-01, -1.28223914e-01, -3.75619248e-02,
         7.08229282e-02,  1.00701328e-01,  2.29645356e-01,
         1.02668842e-01, -6.29047896e-01, -5.58715957e-02,
         1.91430608e-02, -3.47071982e-01,  7.27731353e-02,
        -2.47059734e-01, -5.26368576e-01,  1.65127341e-01,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
       [-9.63067753e-02, -1.61176470e-01,  3.61049346e-01,
        -5.11112334e-01,  5.67850199e-01,  4.33443342e-01,
        -3.50807074e-02,  1.52170315e-01, -1.55562097e-01,
         1.79190166e-02, -1.72897257e-02, -7.90351905e-02,
        -3.54950262e-02,  7.44224684e-02,  2.40106079e-02,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
       [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         1.00000000e+00,  0.00000000e+00,  0.00000000e+00],
       [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         0.00000000e+00,  1.00000000e+00,  0.00000000e+00],
       [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  1.00000000e+00],
       [ 2.54307728e-01, -1.42146362e-02, -1.29741481e-01,
         9.47367593e-02,  1.48502635e-01,  3.12213442e-01,
         3.07042299e-02,  1.77477992e-01,  5.12379132e-01,
         1.70964658e-01, -7.56132131e-02,  2.94437322e-01,
         5.80347432e-01, -1.55418977e-01,  1.10525928e-01,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
       [ 3.01373661e-02, -2.63216818e-01,  7.11948734e-02,
         9.31761314e-02,  1.39689281e-01, -1.14265371e-01,
         4.07925969e-02,  6.59062127e-02, -1.42541755e-01,
        -3.56639552e-01,  2.46293515e-01,  7.76867539e-01,
        -1.26750877e-01, -7.49519350e-02, -2.10008670e-01,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
       [-3.17285197e-02,  2.59437632e-02,  1.54275150e-04,
         2.38561981e-02, -4.67095181e-03, -5.89522109e-02,
         1.34852418e-01,  8.72002606e-02, -6.28809797e-02,
         7.46512734e-01, -1.48146495e-01,  3.90174634e-01,
        -3.32217403e-01,  2.88890376e-01,  1.98040093e-01,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00]])