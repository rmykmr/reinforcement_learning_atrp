'''
List of registered environment names in this file:

ATRP-psnt-td-bimodal-v0
ATRP-psnt-td-tailing-v0
ATRP-psnt-td-step_left-v0
ATRP-psnt-td-step_right-v0
ATRP-psnt-td-flat_wide-v0
ATRP-psnt-td-flat_narrow-v0

ATRP-pst-td-bimodal-v0
ATRP-pst-td-tailing-v0
ATRP-pst-td-step_left-v0
ATRP-pst-td-step_right-v0
ATRP-pst-td-flat_wide-v0
ATRP-pst-td-flat_narrow-v0

ATRP-psnt-td-srcg-bimodal-v0
ATRP-psnt-td-srcg-tailing-v0
ATRP-psnt-td-srcg-step_left-v0
ATRP-psnt-td-srcg-step_right-v0
ATRP-psnt-td-srcg-flat_wide-v0
ATRP-psnt-td-srcg-flat_narrow-v0

ATRP-pst-td-srcg-bimodal-v0
ATRP-pst-td-srcg-tailing-v0
ATRP-pst-td-srcg-step_left-v0
ATRP-pst-td-srcg-step_right-v0
ATRP-pst-td-srcg-flat_wide-v0
ATRP-pst-td-srcg-flat_narrow-v0
'''

'''
Diverse shape control environments
'''
from register_targets import register_targets


''' Two-level reward environments. +0.1 if close, +1.0 if very close. '''
kwargs_common = dict(
    max_rad_len=100,
    step_time=5e2,
    completion_time=1e5,
    min_steps=100,
    termination=None, # must be set later
    k_prop=1.6e3,
    k_act=0.45,
    k_deact=1.1e7,
    k_ter=1e8,
    mono_init=0.0,
    cu1_init=0.0,
    cu2_init=0.0,
    dorm1_init=0.0,
    mono_unit=0.1,
    cu1_unit=0.004,
    cu2_unit=0.004,
    dorm1_unit=0.008,
    mono_cap=10.0,
    cu1_cap=0.2,
    cu2_cap=0.2,
    dorm1_cap=0.4,
    mono_density=8.73,
    sol_init=0.01,
    sol_cap=0.0,
    reward_chain_type='dorm',
    reward_loose=0.1,
    reward_tight=1.0,
    thres_loose=1e-2,
    thres_tight=3e-3,)

bimodal = [     2.68046413e-08, 4.32424205e-07, 3.49446663e-06, 1.88633832e-05,
                7.65320984e-05, 2.48974902e-04, 6.76658635e-04, 1.58059726e-03,
                3.24031719e-03, 5.92461580e-03, 9.78654072e-03, 1.47610183e-02,
                2.05151053e-02, 2.64856847e-02, 3.20029462e-02, 3.64594815e-02,
                3.94648388e-02, 4.09330091e-02, 4.10791986e-02, 4.03365129e-02,
                3.92275830e-02, 3.82334031e-02, 3.76935020e-02, 3.77552921e-02,
                3.83737652e-02, 3.93506976e-02, 4.03967484e-02, 4.11994404e-02,
                4.14831453e-02, 4.10520223e-02, 3.98120065e-02, 3.77724776e-02,
                3.50315804e-02, 3.17510504e-02, 2.81268117e-02, 2.43608269e-02,
                2.06381172e-02, 1.71110298e-02, 1.38911278e-02, 1.10477946e-02,
                8.61190281e-03, 6.58264344e-03, 4.93575390e-03, 3.63174160e-03,
                2.62315577e-03, 1.86039482e-03, 1.29589284e-03, 8.86780265e-04,
                5.96261910e-04, 3.94018425e-04, 2.55937322e-04, 1.63442119e-04,
                1.02631569e-04, 6.33806393e-05, 3.85001501e-05, 2.30075245e-05,
                1.35285389e-05, 7.82848789e-06, 4.45886172e-06, 2.50013287e-06,
                1.38028768e-06, 7.50444491e-07, 4.01869795e-07, 2.12004766e-07,
                1.10198344e-07, 5.64480999e-08, 2.84999313e-08, 1.41851375e-08,
                6.96134333e-09, 3.36896278e-09, 1.60811160e-09, 7.57225607e-10,
                3.51799292e-10, 1.61285617e-10, 7.29788068e-11, 3.25961772e-11,
                1.43738341e-11, 6.25865132e-12, 2.69126234e-12, 1.14304224e-12,
                4.79581194e-13, 1.98800342e-13, 8.14305857e-14, 3.29634471e-14,
                1.31889541e-14, 5.21648168e-15, 2.03981326e-15, 7.88684391e-16,
                3.01557290e-16, 1.14036205e-16, 4.26553559e-17, 1.57838455e-17,
                5.77843281e-18, 2.09321527e-18, 7.50363933e-19, 2.66214043e-19,
                9.34838845e-20, 3.24963264e-20, 1.11832391e-20, 3.81048303e-21]

tailing = [     1.10999958e-09, 2.16874731e-08, 2.12352765e-07, 1.38949029e-06,
                6.83602903e-06, 2.69764201e-05, 8.89572583e-05, 2.52167665e-04,
                6.27375998e-04, 1.39189758e-03, 2.78869947e-03, 5.09760479e-03,
                8.57452323e-03, 1.33685951e-02, 1.94413458e-02, 2.65185291e-02,
                3.40991211e-02, 4.15279494e-02, 4.81159194e-02, 5.32744504e-02,
                5.66258124e-02, 5.80599876e-02, 5.77269609e-02, 5.59732846e-02,
                5.32462104e-02, 4.99937773e-02, 4.65851717e-02, 4.32656331e-02,
                4.01484995e-02, 3.72373743e-02, 3.44659412e-02, 3.17419862e-02,
                2.89847216e-02, 2.61489319e-02, 2.32341669e-02, 2.02810014e-02,
                1.73586358e-02, 1.45487789e-02, 1.19301430e-02, 9.56651676e-03,
                7.49980438e-03, 5.74802285e-03, 4.30729799e-03, 3.15643607e-03,
                2.26261788e-03, 1.58702209e-03, 1.08958107e-03, 7.32478901e-04,
                4.82333257e-04, 3.11224829e-04, 1.96849268e-04, 1.22090394e-04,
                7.42796938e-05, 4.43454521e-05, 2.59874849e-05, 1.49540061e-05,
                8.45214670e-06, 4.69382331e-06, 2.56192749e-06, 1.37471793e-06,
                7.25420011e-07, 3.76542039e-07, 1.92309474e-07, 9.66636043e-08,
                4.78309363e-08, 2.33047080e-08, 1.11832889e-08, 5.28671322e-09,
                2.46257054e-09, 1.13050365e-09, 5.11595384e-10, 2.28265933e-10,
                1.00438785e-10, 4.35904510e-11, 1.86634650e-11, 7.88466909e-12,
                3.28732122e-12, 1.35283081e-12, 5.49617768e-13, 2.20478065e-13,
                8.73427749e-14, 3.41753879e-14, 1.32096415e-14, 5.04457249e-15,
                1.90360377e-15, 7.09919669e-16, 2.61687211e-16, 9.53575777e-17,
                3.43545915e-17, 1.22384772e-17, 4.31159436e-18, 1.50234615e-18,
                5.17816925e-19, 1.76566365e-19, 5.95683404e-20, 1.98860276e-20,
                6.56982476e-21, 2.14822587e-21, 6.95300815e-22, 2.22780653e-22]

step_left = [   2.70572306e-07, 3.62587623e-06, 2.43448273e-05, 1.09220687e-04,
                3.68457204e-04, 9.97337807e-04, 2.25737995e-03, 4.39718933e-03,
                7.53113403e-03, 1.15338164e-02, 1.60161844e-02, 2.04126167e-02,
                2.41495493e-02, 2.68238720e-02, 2.83181960e-02, 2.88154055e-02,
                2.87211908e-02, 2.85352207e-02, 2.87188789e-02, 2.95952784e-02,
                3.12976782e-02, 3.37654921e-02, 3.67770128e-02, 4.00042737e-02,
                4.30758717e-02, 4.56360633e-02, 4.73918832e-02, 4.81437822e-02,
                4.77988132e-02, 4.63682298e-02, 4.39531596e-02, 4.07227168e-02,
                3.68887541e-02, 3.26807517e-02, 2.83234473e-02, 2.40189184e-02,
                1.99340318e-02, 1.61934839e-02, 1.28780693e-02, 1.00273384e-02,
                7.64548704e-03, 5.70917129e-03, 4.17598394e-03, 2.99252859e-03,
                2.10133006e-03, 1.44615915e-03, 9.75661683e-04, 6.45423279e-04,
                4.18752718e-04, 2.66530784e-04, 1.66466075e-04, 1.02048503e-04,
                6.14193558e-05, 3.63025722e-05, 2.10774915e-05, 1.20244509e-05,
                6.74203444e-06, 3.71628882e-06, 2.01433943e-06, 1.07391717e-06,
                5.63290248e-07, 2.90752436e-07, 1.47723112e-07, 7.38940706e-08,
                3.64004443e-08, 1.76618982e-08, 8.44300558e-09, 3.97721389e-09,
                1.84660471e-09, 8.45222019e-10, 3.81466264e-10, 1.69790904e-10,
                7.45466371e-11, 3.22906977e-11, 1.38019656e-11, 5.82230667e-12,
                2.42445678e-12, 9.96716954e-13, 4.04611575e-13, 1.62212058e-13,
                6.42353358e-14, 2.51291005e-14, 9.71306855e-15, 3.71001367e-15,
                1.40054035e-15, 5.22609014e-16, 1.92787136e-16, 7.03163771e-17,
                2.53611132e-17, 9.04624608e-18, 3.19161427e-18, 1.11390155e-18,
                3.84617451e-19, 1.31403579e-19, 4.44253271e-20, 1.48644032e-20,
                4.92271732e-21, 1.61379773e-21, 5.23751589e-22, 1.68297635e-22]

step_right = [  3.50868114e-08, 5.58100953e-07, 4.44749400e-06, 2.36811091e-05,
                9.48098545e-05, 3.04540988e-04, 8.17856221e-04, 1.88962733e-03,
                3.83638141e-03, 6.95680961e-03, 1.14164639e-02, 1.71392369e-02,
                2.37568045e-02, 3.06483958e-02, 3.70656674e-02, 4.23014806e-02,
                4.58454852e-02, 4.74791759e-02, 4.72901662e-02, 4.56148511e-02,
                4.29380926e-02, 3.97835045e-02, 3.66211070e-02, 3.38068444e-02,
                3.15565728e-02, 2.99489711e-02, 2.89481032e-02, 2.84361033e-02,
                2.82481749e-02, 2.82045001e-02, 2.81359409e-02, 2.79022243e-02,
                2.74025766e-02, 2.65795905e-02, 2.54175837e-02, 2.39369279e-02,
                2.21858705e-02, 2.02312563e-02, 1.81493458e-02, 1.60176338e-02,
                1.39082563e-02, 1.18832659e-02, 9.99179466e-03, 8.26892614e-03,
                6.73597077e-03, 5.40178117e-03, 4.26473756e-03, 3.31506695e-03,
                2.53721738e-03, 1.91207635e-03, 1.41889220e-03, 1.03682098e-03,
                7.46074833e-04, 5.28689713e-04, 3.68958276e-04, 2.53590370e-04,
                1.71669086e-04, 1.14467922e-04, 7.51865745e-05, 4.86516838e-05,
                3.10167669e-05, 1.94840732e-05, 1.20613047e-05, 7.35850852e-06,
                4.42505382e-06, 2.62322254e-06, 1.53319029e-06, 8.83607749e-07,
                5.02209646e-07, 2.81535582e-07, 1.55691784e-07, 8.49462710e-08,
                4.57332006e-08, 2.42990984e-08, 1.27433223e-08, 6.59738227e-09,
                3.37224705e-09, 1.70211060e-09, 8.48473462e-10, 4.17764687e-10,
                2.03202208e-10, 9.76535232e-11, 4.63734106e-11, 2.17635549e-11,
                1.00954933e-11, 4.62933447e-12, 2.09873892e-12, 9.40809681e-13,
                4.17063725e-13, 1.82857688e-13, 7.93023747e-14, 3.40229860e-14,
                1.44418272e-14, 6.06575248e-15, 2.52120702e-15, 1.03714916e-15,
                4.22308249e-16, 1.70223476e-16, 6.79291178e-17, 2.68400543e-17]

flat_wide = [   1.93264031e-06, 1.98884838e-05, 1.03193644e-04, 3.60818841e-04,
                9.59348796e-04, 2.07665508e-03, 3.82939689e-03, 6.21968293e-03,
                9.13522161e-03, 1.23983573e-02, 1.58283530e-02, 1.92808797e-02,
                2.26518616e-02, 2.58574139e-02, 2.88119108e-02, 3.14210267e-02,
                3.35938369e-02, 3.52665055e-02, 3.64247690e-02, 3.71140550e-02,
                3.74322803e-02, 3.75075801e-02, 3.74683651e-02, 3.74147090e-02,
                3.73984428e-02, 3.74158295e-02, 3.74129127e-02, 3.73006861e-02,
                3.69756315e-02, 3.63408874e-02, 3.53240369e-02, 3.38888523e-02,
                3.20399027e-02, 2.98203870e-02, 2.73046569e-02, 2.45875028e-02,
                2.17723897e-02, 1.89605261e-02, 1.62420966e-02, 1.36903485e-02,
                1.13586313e-02, 9.28004949e-03, 7.46912172e-03, 5.92474656e-03,
                4.63380830e-03, 3.57487502e-03, 2.72159427e-03, 2.04554697e-03,
                1.51845461e-03, 1.11373656e-03, 8.07482637e-04, 5.78943007e-04,
                4.10650629e-04, 2.88287466e-04, 2.00391087e-04, 1.37979052e-04,
                9.41482581e-05, 6.36879145e-05, 4.27294106e-05, 2.84445481e-05,
                1.87952205e-05, 1.23322459e-05, 8.03801571e-06, 5.20628345e-06,
                3.35222886e-06, 2.14642046e-06, 1.36714015e-06, 8.66489569e-07,
                5.46630265e-07, 3.43340425e-07, 2.14768708e-07, 1.33825476e-07,
                8.30861241e-08, 5.14083616e-08, 3.17060387e-08, 1.94955107e-08,
                1.19532908e-08, 7.30922151e-09, 4.45811355e-09, 2.71261692e-09,
                1.64679611e-09, 9.97603440e-10, 6.03103457e-10, 3.63904227e-10,
                2.19172601e-10, 1.31773736e-10, 7.90954920e-11, 4.74011832e-11,
                2.83643697e-11, 1.69485786e-11, 1.01133997e-11, 6.02684966e-12,
                3.58704203e-12, 2.13234424e-12, 1.26611473e-12, 7.50934981e-13,
                4.44900088e-13, 2.63311540e-13, 1.55682687e-13, 9.19579928e-14]

flat_narrow = [ 3.75501718e-09, 6.82300984e-08, 6.21072854e-07, 3.77653431e-06,
                1.72594238e-05, 6.32437706e-05, 1.93574734e-04, 5.09110398e-04,
                1.17471051e-03, 2.41617555e-03, 4.48649614e-03, 7.59933784e-03,
                1.18450391e-02, 1.71197167e-02, 2.31012104e-02, 2.92919179e-02,
                3.51228043e-02, 4.00870364e-02, 4.38583476e-02, 4.63545763e-02,
                4.77277998e-02, 4.82891929e-02, 4.83979421e-02, 4.83518638e-02,
                4.83117696e-02, 4.82764660e-02, 4.81074994e-02, 4.75886336e-02,
                4.64981846e-02, 4.46731361e-02, 4.20503847e-02, 3.86793253e-02,
                3.47082635e-02, 3.03527833e-02, 2.58564439e-02, 2.14533801e-02,
                1.73395870e-02, 1.36561182e-02, 1.04841789e-02, 7.84980994e-03,
                5.73474465e-03, 4.08994715e-03, 2.84897765e-03, 1.93929797e-03,
                1.29061275e-03, 8.40135207e-04, 5.35184711e-04, 3.33773771e-04,
                2.03882826e-04, 1.22030466e-04, 7.15958486e-05, 4.11913344e-05,
                2.32478517e-05, 1.28757788e-05, 7.00047011e-06, 3.73755872e-06,
                1.96017624e-06, 1.01014319e-06, 5.11659985e-07, 2.54809942e-07,
                1.24798491e-07, 6.01281901e-08, 2.85060373e-08, 1.33013605e-08,
                6.11030638e-09, 2.76402282e-09, 1.23149573e-09, 5.40548717e-10,
                2.33798977e-10, 9.96663834e-11, 4.18835064e-11, 1.73545375e-11,
                7.09159282e-12, 2.85836743e-12, 1.13662295e-12, 4.45982035e-13,
                1.72701990e-13, 6.60132101e-14, 2.49109631e-14, 9.28211954e-15,
                3.41562230e-15, 1.24144064e-15, 4.45739669e-16, 1.58124815e-16,
                5.54300019e-17, 1.92033552e-17, 6.57592019e-18, 2.22608438e-18,
                7.45057073e-19, 2.46579054e-19, 8.07042117e-20, 2.61254070e-20,
                8.36583111e-21, 2.65024171e-21, 8.30696457e-22, 2.57649193e-22,
                7.90847645e-23, 2.40260041e-23, 7.22505355e-24, 2.15088200e-24]


target_list = [('bimodal', bimodal),            ('tailing', tailing),
               ('step_left', step_left),        ('step_right', step_right),
               ('flat_narrow', flat_narrow),    ('flat_wide', flat_wide)]
'''
No-termination, no-noise envs
'''
kwargs_nt_common = kwargs_common.copy()
kwargs_nt_common['termination'] = False
register_targets(kwargs_nt_common, 'psnt-td', target_list)


'''
With-termination, no-noise envs
'''
kwargs_t_common = kwargs_nt_common.copy()
kwargs_t_common['termination'] = True
register_targets(kwargs_t_common, 'pst-td', target_list)


'''
Gaussian variance control environments with "simulated realistic concerns"
(i.e., noises), gaussian noise version
All currently implemented noises are turned on, including:
    step_time_noise = 0.03  : gaussian sigma = 1% noise in step_time;
    k_noise = 0.3           : gaussian sigma = 10% noise in all rate constants;
    obs_noise = 3e-3        : gaussian sigma = 1e-3 noise on observations;
    addition_noise = 0.03   : gaussian sigma = 1% noise in addition unit amount.
'''

'''
No-termination, srcg-noise envs
'''
kwargs_nt_srcg_common = kwargs_nt_common.copy()
kwargs_nt_srcg_common['step_time_noise'] = 'gaussian', 0.03
kwargs_nt_srcg_common['k_noise'] = 'gaussian', 0.3
kwargs_nt_srcg_common['obs_noise'] = 'gaussian', 3e-3
kwargs_nt_srcg_common['addition_noise'] = 'gaussian', 0.03
kwargs_nt_srcg_common['render_obs'] = 'dorm', (8, 108)
register_targets(kwargs_nt_srcg_common, 'psnt-td-srcg', target_list)


'''
With-termination, srcg-noise envs
'''
kwargs_t_srcg_common = kwargs_nt_srcg_common.copy()
kwargs_t_srcg_common['termination'] = True
register_targets(kwargs_t_srcg_common, 'pst-td-srcg', target_list)

