from LinkedIn import LinkedIn
import getpass

url_list = ["https://www.linkedin.com/in/lassebirkolesen", "https://www.linkedin.com/in/s%C3%B8ren-holbech-8313b01", "https://www.linkedin.com/in/daniel-hansen-68a53111", "https://www.linkedin.com/in/niels-kristian-bitsch-0b71a319", "https://www.linkedin.com/in/morteniversen", "https://www.linkedin.com/in/bjarkestaun", "https://www.linkedin.com/in/anja-egelund-m%C3%BCller-5123802", "https://www.linkedin.com/in/hanjak", "https://www.linkedin.com/in/stineuldbjerghansen", "https://www.linkedin.com/in/carstentradssorensen", "https://www.linkedin.com/in/thomas-ballegaard-407a751", "https://www.linkedin.com/in/smunken", "https://www.linkedin.com/in/nielsvejrupcarlsen", "https://www.linkedin.com/in/soerenhechtpetersen", "https://www.linkedin.com/in/mathilde-vejn%C3%B8-lund-a2474975", "https://www.linkedin.com/in/hans-munk-97326632", "https://www.linkedin.com/in/anders-s%C3%B8e-jensen-9584925", "https://www.linkedin.com/in/lisbeth-kattenh%C3%B8j-35a3722", "https://www.linkedin.com/in/egelundjens", "https://www.linkedin.com/in/vonhaller", "https://www.linkedin.com/in/sorendhansen", "https://www.linkedin.com/in/jamila-ahdidan-a8890b5", "https://www.linkedin.com/in/daniel-langhoff-758a689", "https://www.linkedin.com/in/lars-henrik-hansen-333b065", "https://www.linkedin.com/in/sten-t-davidsen-aa3914", "https://www.linkedin.com/in/claus-moltrup-1238961b", "https://www.linkedin.com/in/erik-laigaard-19b8aa4b", "https://www.linkedin.com/in/jeffrey-walter-7422b683", "https://www.linkedin.com/in/holger-ross-lauritsen-a64ab951", "https://www.linkedin.com/in/mfsorensen", "https://www.linkedin.com/in/madsva", "https://www.linkedin.com/in/erik-persson-17148066", "https://www.linkedin.com/in/thorjespersen", "https://www.linkedin.com/in/henrikdurr", "https://www.linkedin.com/in/madsemilmatthiesen", "https://www.linkedin.com/in/larskolind", "https://www.linkedin.com/in/peter-gr%C3%B8ftehauge-61275313", "https://www.linkedin.com/in/peter-max-b37774", "https://www.linkedin.com/in/peter-bisgaard-039a80ab", "https://www.linkedin.com/in/tromholt", "https://www.linkedin.com/in/jens-liebst-aa4054b4", "https://www.linkedin.com/in/kaj-andersen-727a02", "https://www.linkedin.com/in/ryan-lauridsen-886b927", "https://www.linkedin.com/in/henriknielsen3", "https://www.linkedin.com/in/mikaelbreinholst", "https://www.linkedin.com/in/s%C3%B8ren-isaksen-741a0989", "https://www.linkedin.com/in/allan-s%C3%B8gaard-larsen-0a7796b3", "https://www.linkedin.com/in/martin-thomsen-789a5396", "https://www.linkedin.com/in/maria-juel-k%C3%A4hler-53bb9", "https://www.linkedin.com/in/carstenwestergaard", "https://www.linkedin.com/in/bjarkebekhoj", "https://www.linkedin.com/in/martinbear", "https://www.linkedin.com/in/lene-gerlach-87426442", "https://www.linkedin.com/in/jesper-bang-j%C3%B8rgensen-1ba09a7", "https://www.linkedin.com/in/wwwmodus2dk", "https://www.linkedin.com/in/morten-mathiesen-4600872", "https://www.linkedin.com/in/jesperlindhardt", "https://www.linkedin.com/in/christiansteffensen", "https://www.linkedin.com/in/cathal-mahon-72176a1a", "https://www.linkedin.com/in/frank-ludvigsen-15617946", "https://www.linkedin.com/in/tim-tim-elmhauge-11b142154", "https://www.linkedin.com/in/michael-jackson-661b25a", "https://www.linkedin.com/in/erik-lorenz-petersen-23052", "https://www.linkedin.com/in/lars-andersen-20363021", "https://www.linkedin.com/in/ekkelund", "https://www.linkedin.com/in/januslindau", "https://www.linkedin.com/in/soerenbruun", "https://www.linkedin.com/in/pernillesolviggraux", "https://www.linkedin.com/in/stefanandreasen", "https://www.linkedin.com/in/helle-skov-lund-a52a4b27", "https://www.linkedin.com/in/lars-thinggaard-7374b3", "https://www.linkedin.com/in/steen-frederiksen-07533719", "https://www.linkedin.com/in/ulrik-j%C3%B8rring-08559", "https://www.linkedin.com/in/runihammer", "https://www.linkedin.com/in/j%C3%B8rgen-drejer-5b7178", "https://www.linkedin.com/in/thomas-feldthus-510543", "https://www.linkedin.com/in/tore-sylvester-jeppesen-6343324", "https://www.linkedin.com/in/richardbreiter", "https://www.linkedin.com/in/rasmusbusk", "https://www.linkedin.com/in/kjolhede", "https://www.linkedin.com/in/dorteskovbo", "https://www.linkedin.com/in/kennethpuggaard", "https://www.linkedin.com/in/marianne-philip-177087a9", "https://www.linkedin.com/in/holledig", "https://www.linkedin.com/in/flemming-g-jensen-2537a41", "https://www.linkedin.com/in/peter-lorens-ravn-a4594261", "https://www.linkedin.com/in/ngundersen", "https://www.linkedin.com/in/sveneric", "https://www.linkedin.com/in/hansgormsen", "https://www.linkedin.com/in/jens-peter-toft-310ab713", "https://www.linkedin.com/in/sorensteenrasmussen", "https://www.linkedin.com/in/s%C3%B8ren-frandsen-38937314", "https://www.linkedin.com/in/birgit-w-n%25C3%25B8rgaard-9a5aa714", "https://www.linkedin.com/in/peerkisbye", "https://www.linkedin.com/in/lene-juel-kjeldsen-b17aa94a", "https://www.linkedin.com/in/hallenborg", "https://www.linkedin.com/in/jmskibsted", "https://www.linkedin.com/in/leif-petersen-6931b66", "https://www.linkedin.com/in/anwar-almojarkesh-52240025", "https://www.linkedin.com/in/larshedemannnielsen", "https://www.linkedin.com/in/frank-hansen-06b4117", "https://www.linkedin.com/in/troelstimm", "https://www.linkedin.com/in/per-juul-nielsen", "https://www.linkedin.com/in/morten-heide-b32b393", "https://www.linkedin.com/in/mogenshafstroemnielsen", "https://www.linkedin.com/in/kristoffergandrup", "https://www.linkedin.com/in/marielouiselittle", "https://www.linkedin.com/in/kbadenk", "https://www.linkedin.com/in/ulrikeriksen", "https://www.linkedin.com/in/prebenstorm", "https://www.linkedin.com/in/dan-robert-larsen-4bb62152", "https://www.linkedin.com/in/alexander-korre-horten-94241628", "https://www.linkedin.com/in/kim-vestergaard-hansen-48686a2", "https://www.linkedin.com/in/martin-lillholm-93a588", "https://www.linkedin.com/in/kennethbengtsson", "https://www.linkedin.com/in/helge-munk-7012714", "https://www.linkedin.com/in/peterfejerskov", "https://www.linkedin.com/in/bjarne-warming-jensen-a4651931", "https://www.linkedin.com/in/anders-kj%C3%A6r-adamsen-7a2158a2", "https://www.linkedin.com/in/claus-fedder-sorensen", "https://www.linkedin.com/in/s%C3%B8ren-jepsen-bb0b366b", "https://www.linkedin.com/in/lars-halkj%25C3%25A6r-1524191", "https://www.linkedin.com/in/line-s%25C3%25B8lvkj%25C3%25A6r-jespersen-8596016", "https://www.linkedin.com/in/anders-hvidgaard-poder-4459495", "https://www.linkedin.com/in/jan-lorentzen-02a8454b", "https://www.linkedin.com/in/niels-bjerregaard-438501", "https://www.linkedin.com/in/henning-sandal-b088011", "https://www.linkedin.com/in/mads-rebsdorf", "https://www.linkedin.com/in/jakob-s%C3%B8rensen-18111442", "https://www.linkedin.com/in/peter-gravesen", "https://www.linkedin.com/in/ces01", "https://www.linkedin.com/in/henrikmoos", "https://www.linkedin.com/in/jesper-andersen-23734710", "https://www.linkedin.com/in/jesperclemmensen", "https://www.linkedin.com/in/laursenthomas", "https://www.linkedin.com/in/bettinaravn", "https://www.linkedin.com/in/svend-aage-hansen-99951240?trk=pub-pbmap", "https://www.linkedin.com/in/cej01", "https://www.linkedin.com/in/per-friis-madsen-989a571a", "https://www.linkedin.com/in/hanschrandersen", "https://www.linkedin.com/in/torben-j%C3%B8rgensen-393890112", "https://www.linkedin.com/in/dorthe-greve-2255b7124?trk=prof-samename-picture", "https://www.linkedin.com/in/niels-heering-129b5590", "https://www.linkedin.com/in/gustaf-iuel-brockdorff-34a55a85", "https://www.linkedin.com/in/erikhougaard", "https://www.linkedin.com/in/tom-olesen-7632717", "https://www.linkedin.com/in/karin-verland-3987023", "https://www.linkedin.com/in/thomas-gravgaard-2a97974", "https://www.linkedin.com/in/henrik-moltke-3092602", "https://www.linkedin.com/in/bobbysoni", "https://www.linkedin.com/in/clausandersson", "https://www.linkedin.com/in/ole-bitsch-jensen-90544", "https://www.linkedin.com/in/mikael-stade-9b78603", "https://www.linkedin.com/in/stenvel", "https://www.linkedin.com/in/jensagerskov", "https://www.linkedin.com/in/sten-scheibye-a82814148", "https://www.linkedin.com/in/claus-h%C3%A9lix-nielsen-337b028", "https://www.linkedin.com/in/leif-jensen-1a46767", "https://www.linkedin.com/in/niels-henrik-jessen-29806a66", "https://www.linkedin.com/in/thomaschrbeck", "https://www.linkedin.com/in/j%C3%B8rgen-toftegaard-59a2345", "https://www.linkedin.com/in/rasmus-thostrup-m%C3%B8ller-23317062", "https://www.linkedin.com/in/arne-fredens-481b8212", "https://www.linkedin.com/in/lars-hummelsh%C3%B8j-78592b1", "https://www.linkedin.com/in/dorte-prip-016a232", "https://www.linkedin.com/in/carsten-ceutz-6a9109", "https://www.linkedin.com/in/mette-vagner-johannesen-73093a20", "https://www.linkedin.com/in/steen-enrico-andersen-6384731", "https://www.linkedin.com/in/maleneschroderdk", "https://www.linkedin.com/in/ulf-s-skimmeland-b24757", "https://www.linkedin.com/in/luke-mercer-0a86177", "https://www.linkedin.com/in/frank-knudsen-4698862", "https://www.linkedin.com/in/mattiasfjellvang", "https://www.linkedin.com/in/pitzner", "https://www.linkedin.com/in/michaelwfrank1", "https://www.linkedin.com/in/larsbokoppler", "https://www.linkedin.com/in/jesper-studsgaard-65b1b32", "https://www.linkedin.com/in/torsten-freltoft-7b85a82", "https://www.linkedin.com/in/bolette-rud-pallesen-31b0745", "https://www.linkedin.com/in/kovaltsenko", "https://www.linkedin.com/in/dan-takiar-petersen-84b84829", "https://www.linkedin.com/in/peder-van-der-schaft-9530402", "https://www.linkedin.com/in/thomasmunksgaard", "https://www.linkedin.com/in/jesperpronk", "https://www.linkedin.com/in/morten-grunnet-8318076", "https://www.linkedin.com/in/lars-gredsted-5652536", "https://www.linkedin.com/in/s%C3%B8ren-stougaard-dalby-b3857a28", "https://www.linkedin.com/in/morten-junker-nielsen-52b3936", "https://www.linkedin.com/in/anders2", "https://www.linkedin.com/in/anne-broeng-27159345", "https://www.linkedin.com/in/jesper-d-christoffersen-17a249", "https://www.linkedin.com/in/lars-christian-hansen-17ab68", "https://www.linkedin.com/in/weiming-jiang-10478633", "https://www.linkedin.com/in/davidmonks", "https://www.linkedin.com/in/gert-zimmer-hansen-17414a", "https://www.linkedin.com/in/eskegunge", "https://www.linkedin.com/in/david-lyager-sch%25C3%25B8ndorff-4b51a8", "https://www.linkedin.com/in/john-svensson-21572359", "https://www.linkedin.com/in/jakobhagemann", "https://www.linkedin.com/in/davidventzel", "https://www.linkedin.com/in/seadbajrovic", "https://www.linkedin.com/in/s%C3%B8ren-brunak-102809", "https://www.linkedin.com/in/morten-lundeh%C3%B8j-m%C3%B8ller-7904b344", "https://www.linkedin.com/in/ole-juul-j%C3%B8rgensen-b6722214", "https://www.linkedin.com/in/poul-krog-s%C3%B8rensen-b3b3451a", "https://www.linkedin.com/in/julie-nielsen-8185831", "https://www.linkedin.com/in/anderberg", "https://www.linkedin.com/in/samandari", "https://www.linkedin.com/in/mmfrederiksen?authType=NAME_SEARCH&authToken=fqDS&locale=en_US&trk=tyah&trkInfo=clickedVertical%3Amynetwork%2CclickedEntityId%3A106205%2CauthType%3ANAME_SEARCH%2Cidx%3A1-1-1%2CtarId%3A1481837758010%2Ctas%3Amartin%20frede", "https://www.linkedin.com/in/bjarkewalling", "https://www.linkedin.com/in/s%C3%B8ren-smed-a280a4126", "https://www.linkedin.com/in/jespertjohansen", "https://www.linkedin.com/in/flodgaard", "https://www.linkedin.com/in/anders-h%C3%B8y-thomsen-b1779022", "https://www.linkedin.com/in/steffenbagge", "https://www.linkedin.com/in/mogensvigpedersen", "https://www.linkedin.com/in/christian-%C3%B8stergaard-885ba954", "https://www.linkedin.com/in/jonaskongslund", "https://www.linkedin.com/in/martin14", "https://www.linkedin.com/in/tolstoy", "https://www.linkedin.com/in/s%25C3%25B8ren-christiansen-79964a1", "https://www.linkedin.com/in/lau-normann-jorgensen-05107111", "https://www.linkedin.com/in/jakob-kesje-a619342", "https://www.linkedin.com/in/flemming-besenbacher-8497353", "https://www.linkedin.com/in/thomasheltborgjuul", "https://www.linkedin.com/in/henning-christensen-5ab70a20", "https://www.linkedin.com/in/thomasbj%C3%B8rnholm", "https://www.linkedin.com/in/mai-britt-zocca-66b70b6", "https://www.linkedin.com/in/leahokland", "https://www.linkedin.com/in/jensvinge", "https://www.linkedin.com/in/kjaersgaardmorten", "https://www.linkedin.com/in/pkrishen", "https://www.linkedin.com/in/afzaalace", "https://www.linkedin.com/in/christianrisom", "https://www.linkedin.com/in/mariola-pytlikova-525739", "https://www.linkedin.com/in/slottrup", "https://www.linkedin.com/in/mette-hejl-3a17922", "https://www.linkedin.com/in/martin-pr%C3%BCss-85b85a1", "https://www.linkedin.com/in/jesper-knudsen-4259b01a", "https://www.linkedin.com/in/christianbowall", "https://www.linkedin.com/in/mkarlsen", "https://www.linkedin.com/in/niels-anker-rasmussen-0b17385", "https://www.linkedin.com/in/henrikaagaard", "https://www.linkedin.com/in/massmiltonengberg", "https://www.linkedin.com/in/brian-poulsen-6a846a44", "https://www.linkedin.com/in/nicholaj-asger-hansen-aa43291", "https://www.linkedin.com/in/karasmussen", "https://www.linkedin.com/in/ole-vitting-petersen-a7ab5a3a", "https://www.linkedin.com/in/lone-bjerre-christensen-51586366", "https://www.linkedin.com/in/mads-bonde-8bb4194", "https://www.linkedin.com/in/tobiasdam", "https://www.linkedin.com/in/clausbonielsen", "https://www.linkedin.com/in/karsten-cronwald-4322553", "https://www.linkedin.com/in/finnvernerjensen", "https://www.linkedin.com/in/richard-humleb%C3%A6k-jensen-2a164913", "https://www.linkedin.com/in/mads-danielsen-b0327883", "https://www.linkedin.com/in/s%C3%B8ren-bruun-24a9283", "https://www.linkedin.com/in/larslundbye", "https://www.linkedin.com/in/mette-therkildsen-49010459", "https://www.linkedin.com/in/gert-skov-petersen-82247", "https://www.linkedin.com/in/poul-andersen-4657484a", "https://www.linkedin.com/in/peterbirkholmbuch", "https://www.linkedin.com/in/elk%C3%A6r-mathiassen-2526222a", "https://www.linkedin.com/in/claus-hansen-0a12413b", "https://www.linkedin.com/in/svend-m%C3%B8ller-nielsen-a0620230", "https://www.linkedin.com/in/henrik-dinnsen-76427844", "https://www.linkedin.com/in/oleklinkby", "https://www.linkedin.com/in/jesper-milthers-2781b64", "https://www.linkedin.com/in/ivanalexander", "https://www.linkedin.com/in/ulriknejsummadsen", "https://www.linkedin.com/in/hans-christian-orlof-petersen-48168b10", "https://www.linkedin.com/in/ove-vestergaard-408a0013", "https://www.linkedin.com/in/klaus-kibsgaard-626b5810", "https://www.linkedin.com/in/mogens-nygaard-05a9746", "https://www.linkedin.com/in/madslind", "https://www.linkedin.com/in/pia-kofoed-jacobsen-b1750415", "https://www.linkedin.com/in/christiansvane", "https://www.linkedin.com/in/peter-pedersen-9a075295", "https://www.linkedin.com/in/jens-nielsen-b841154", "https://www.linkedin.com/in/larskuch", "https://www.linkedin.com/in/jesper-kuch-flod-pedersen-4175b3", "https://www.linkedin.com/in/rasmus-wilhelmsen-a674534", "https://www.linkedin.com/in/flemming-m%C3%B8ller-jensen-b67569123", "https://www.linkedin.com/in/susann-hauschildt-b38ab487", "https://www.linkedin.com/in/lars-hallgren-0511a74", "https://www.linkedin.com/in/jesperahlmannandersen", "https://www.linkedin.com/in/lineholtenreimer", "https://www.linkedin.com/in/s%C3%B8ren-ingerslev-4a923b", "https://www.linkedin.com/in/susanne-lundvald-63bab94", "https://www.linkedin.com/in/wiggin", "https://www.linkedin.com/in/yury-birchenko-2a20b24", "https://www.linkedin.com/in/marianne-tochtermann-6243a41", "https://www.linkedin.com/in/runarlie", "https://www.linkedin.com/in/michael-brock-45bb7a3b?authType=name&authToken=shNN&locale=en_US&srchid=1488127641476270908906&srchindex=17&srchtotal=19&trk=vsrp_people_res_name&trkInfo=VSRPsearchId%3A1488127641476270908906%2CVSRPtargetId%3A143241479%2CVSRPcmpt%3Aprimary%2CVSRPnm%3Afalse%2CauthType%3Aname", "https://www.linkedin.com/in/j%25C3%25B8rn-kofoed-m%25C3%25B8ller-a71a832", "https://www.linkedin.com/in/stig-christensen-7558b023", "https://www.linkedin.com/in/peteregehoved", "https://www.linkedin.com/in/lisa-dam-6541a3155", "https://www.linkedin.com/in/hans-steenberg-7429ba5", "https://www.linkedin.com/in/maltebreiting", "https://www.linkedin.com/in/jakobnoergaard", "https://www.linkedin.com/in/eskholm", "https://www.linkedin.com/in/mikkelclausen", "https://www.linkedin.com/in/mortendamgaard", "https://www.linkedin.com/in/anders-tvegaard-3305a1", "https://www.linkedin.com/in/thomassugar", "https://www.linkedin.com/in/kristian-dahl-hansen-0872143", "https://www.linkedin.com/in/nikolaikronborg", "https://www.linkedin.com/in/rikke-westh-thon-0397389", "https://www.linkedin.com/in/jens-ellegaard-1053366", "https://www.linkedin.com/in/jenslohfert", "https://www.linkedin.com/in/christian-fink-hansen-9a20216", "https://www.linkedin.com/in/pederburgaard", "https://www.linkedin.com/in/henrik-skovgaard", "https://www.linkedin.com/in/tina-rosholm-237275", "https://www.linkedin.com/in/jesper-holmgaard-0395b931", "https://www.linkedin.com/in/henrik-marinus-pedersen-b10b9aa", "https://www.linkedin.com/in/ankedomdey", "https://www.linkedin.com/in/flemminghartvigpedersen", "https://www.linkedin.com/in/camillaleyvalentin", "https://www.linkedin.com/in/martinpronk", "https://www.linkedin.com/in/claus-dyre-11122960", "https://www.linkedin.com/in/hans-h-jochumsen-b00860", "https://www.linkedin.com/in/jan-madsen-ba91786", "https://www.linkedin.com/in/henrik-kirketerp-7ba298b", "https://www.linkedin.com/in/poul-lading", "https://www.linkedin.com/in/martin-h%C3%B8j-lauridsen-92257a42", "https://www.linkedin.com/in/peterladefoged", "https://www.linkedin.com/in/lars-enevoldsen-7a36753?authType=NAME_SEARCH&authToken=2iqv&locale=en_US&trk=tyah&trkInfo=clickedVertical%3Amynetwork%2CclickedEntityId%3A10605867%2CauthType%3ANAME_SEARCH%2Cidx%3A2-1-4%2CtarId%3A1455532922078%2Ctas%3Alars%20enee", "https://www.linkedin.com/in/mbisgaard", "https://www.linkedin.com/in/allan-asp-poulsen-13b40762", "https://www.linkedin.com/in/niels-holm-50b5306a", "https://www.linkedin.com/in/s%C3%B8ren-m%C3%B8ller-spring-2a277758", "https://www.linkedin.com/in/thorkild-larsen-910a4452", "https://www.linkedin.com/in/kennethhelmerlarsen", "https://www.linkedin.com/in/mortensoltoft", "https://www.linkedin.com/in/bjerrebojsen", "https://www.linkedin.com/in/gadeinc", "https://www.linkedin.com/in/ssvandel", "https://www.linkedin.com/in/jan-h%C3%B8jsgaard-46673a6", "https://www.linkedin.com/in/henrikhjorth", "https://www.linkedin.com/in/hans-tino-hansen-40b92a", "https://www.linkedin.com/in/webermorten", "https://www.linkedin.com/in/stig-streit-jensen-1836395", "https://www.linkedin.com/in/jan-holm-8494119", "https://www.linkedin.com/in/thomas-jam-pedersen-9595a4", "https://www.linkedin.com/in/hanne-bender-66761b3", "https://www.linkedin.com/in/janhjortshoej", "https://www.linkedin.com/in/michael-alstr%C3%B8m-06b40a22", "https://www.linkedin.com/in/jens-dall-bentzen-6346b66", "https://www.linkedin.com/in/lars-n%C3%B8rgaard-bj%C3%B8rn-9419293", "https://www.linkedin.com/in/martinlumbye", "https://www.linkedin.com/in/jesperbakolesen", "https://www.linkedin.com/in/eric-korre-horten-ba8509", "https://www.linkedin.com/in/elsebethaagaard", "https://www.linkedin.com/in/anders-%C3%B8rjan-jensen-5507b4", "https://www.linkedin.com/in/flemming-bastholm-93939b7", "https://www.linkedin.com/in/kasper-daae-74277478", "https://www.linkedin.com/in/kurt-erling-birk-61500622", "https://www.linkedin.com/in/jakob-fuglede-nielsen-9ab51b2", "https://www.linkedin.com/in/blauenfeldt", "https://www.linkedin.com/in/martin-koch-4a1685", "https://www.linkedin.com/in/sorenschoennemann", "https://www.linkedin.com/in/kwamedako", "https://www.linkedin.com/in/jens-overgaard-46019a22", "https://www.linkedin.com/in/clausrisager?authType=NAME_SEARCH&authToken=oab3&locale=en_US&trk=tyah&trkInfo=clickedVertical%3Amynetwork%2CclickedEntityId%3A31182666%2CauthType%3ANAME_SEARCH%2Cidx%3A1-1-1%2CtarId%3A1472735616817%2Ctas%3AClaus%20Risager", "https://www.linkedin.com/in/rene-dencker-eriksen-184730", "https://www.linkedin.com/in/jesper-haugaard-b73a225", "https://www.linkedin.com/in/klaus-kalstrup-7676b8", "https://www.linkedin.com/in/jens-munch-hansen-39b9a711b", "https://www.linkedin.com/in/ukwiil", "https://www.linkedin.com/in/jens-paludan-9aab3477", "https://www.linkedin.com/in/j%C3%B8rgen-granborg-6866a12", "https://www.linkedin.com/in/finn-lynge-jepsen-63544715", "https://www.linkedin.com/in/niels-kollerup-6024822", "https://www.linkedin.com/in/claus-bo-andersen-a713a317", "https://www.linkedin.com/in/clauschr", "https://www.linkedin.com/in/peter-michael-oxholm-zigler-9373603", "https://www.linkedin.com/in/alaustsen?authType=OPENLINK&authToken=jCeC&locale=da_DK&srchid=3474615251465499993205&srchindex=1&srchtotal=13&trk=vsrp_people_res_name&trkInfo=VSRPsearchId%3A3474615251465499993205%2CVSRPtargetId%3A44760403%2CVSRPcmpt%3Aprimary%2CVSRPnm%3Atrue%2CauthType%3AOPENLINK", "https://www.linkedin.com/in/larsbarkholt", "https://www.linkedin.com/in/poul-ernst-rasmussen-ba682356", "https://www.linkedin.com/in/jakobsand", "https://www.linkedin.com/in/lars-baun-1b787", "https://www.linkedin.com/in/jespermuellerkrogstrup", "https://www.linkedin.com/in/chrelbek", "https://www.linkedin.com/in/gorml", "https://www.linkedin.com/in/henrikhpedersen", "https://www.linkedin.com/in/jens-holm-m%C3%B8ller-8445874", "https://www.linkedin.com/in/thomas-harrit-ba91234", "https://www.linkedin.com/in/sanne-bang-olsen-3567372", "https://www.linkedin.com/in/alrasmussen", "https://www.linkedin.com/in/olelangvadwessby", "https://www.linkedin.com/in/larserasmussen", "https://www.linkedin.com/in/henrik-harboe-9a0a63b", "https://www.linkedin.com/in/thomas-ryge-mikkelsen-831987", "https://www.linkedin.com/in/mrasmussen3", "https://www.linkedin.com/in/claus-nielsen-a8a7664b", "https://www.linkedin.com/in/thomas-pedersen-tp-1377522", "https://www.linkedin.com/in/rasmusjensen2", "https://www.linkedin.com/in/mkmikkelsen", "https://www.linkedin.com/in/s%C3%B8ren-n%C3%B8rg%C3%A5rd-b8b85354", "https://www.linkedin.com/in/mikkelbachmortensen", "https://www.linkedin.com/in/kristinajensen1", "https://www.linkedin.com/in/asserfemoe", "https://www.linkedin.com/in/justin-holley-27872a4", "https://www.linkedin.com/in/bjarne-henning-jensen-95b6131", "https://www.linkedin.com/in/claus-bengtsson", "https://www.linkedin.com/in/christianlundsorensen", "https://www.linkedin.com/in/niels-lysholm-engelhard-a98319", "https://www.linkedin.com/in/laura-hay-186a012", "https://www.linkedin.com/in/karin-absalonsen-09a1ab146", "https://www.linkedin.com/in/claus-birger-s%C3%B8rensen-419a8b1", "https://www.linkedin.com/in/martin-aagesen-4a549b4", "https://www.linkedin.com/in/gert-bolander-jensen-60a01b2", "https://www.linkedin.com/in/s%C3%B8ren-henningsen-479bb810b", "https://www.linkedin.com/in/karl-erik-thomsen-8828b5153", "https://www.linkedin.com/in/lone-hoppe-86884588", "https://www.linkedin.com/in/lars-jarnbo-pedersen-2b4a2b", "https://www.linkedin.com/in/lone-gammelgaard-schwarz-41b6b91", "https://www.linkedin.com/in/peterperregaard", "https://www.linkedin.com/in/kasper-roseeuw-poulsen-431883", "https://www.linkedin.com/in/stig-loekke-pedersen-710927", "https://www.linkedin.com/in/rasmus-vendler-toft-kehler-419157", "https://www.linkedin.com/in/astrid-sommer-a767952b", "https://www.linkedin.com/in/harry-christopher-riekehr-14456960", "https://www.linkedin.com/in/rtaaning", "https://www.linkedin.com/in/anders-thyboe-lindhardt-a755584", "https://www.linkedin.com/in/per-knudsen-435205", "https://www.linkedin.com/in/jan-h%25C3%25B8jbjerg-jensen-35baa781", "https://www.linkedin.com/in/pawanmarwahacornell", "https://www.linkedin.com/in/madsstenhoj", "https://www.linkedin.com/in/andreas-koefoed-hansen-a5177238", "https://www.linkedin.com/in/tim-langer-rasmussen-90554547", "https://www.linkedin.com/in/mortenfindlaerkholm", "https://www.linkedin.com/in/ulrikhjorth", "https://www.linkedin.com/in/kasperheine", "https://www.linkedin.com/in/frank-espersen-82708210", "https://www.linkedin.com/in/peter-holten-muhlmann-9825992", "https://www.linkedin.com/in/lone-sejersen-a01a493", "https://www.linkedin.com/in/michael-helmersh%C3%B8j-7831ab33", "https://www.linkedin.com/in/michael-thorndahl-simmelsgaard-0a84197", "https://www.linkedin.com/in/larsribe", "https://www.linkedin.com/in/ole-bigum-nielsen-aa489a19", "https://www.linkedin.com/in/jeppe-zink-5a85305", "https://www.linkedin.com/in/kllund", "https://www.linkedin.com/in/tokegrofte", "https://www.linkedin.com/in/andersholmejensen", "https://www.linkedin.com/in/lars-bo-brink-084a7a46", "https://www.linkedin.com/in/ole-green-38a5a63", "https://www.linkedin.com/in/peter-lauridsen-4b053216", "https://www.linkedin.com/in/andersensten", "https://www.linkedin.com/in/ove-g-rasmussen-91520236", "https://www.linkedin.com/in/lars-henriksen-4ab07723", "https://www.linkedin.com/in/per-ravn-071046a6", "https://www.linkedin.com/in/hans-ulrik-n%C3%B8rgaard-948183", "https://www.linkedin.com/in/macgundel", "https://www.linkedin.com/in/mogensmoeller", "https://www.linkedin.com/in/lasse-eskildsen-6a8a2b57", "https://www.linkedin.com/in/hans-henrik-obel-b67a0349", "https://www.linkedin.com/in/sorenspellinglund", "https://www.linkedin.com/in/hasse-hunskj%C3%A6r-69325638", "https://www.linkedin.com/in/hans-iakob-estrup-b00b731", "https://www.linkedin.com/in/poul-sloth-petersen-6a74359", "https://www.linkedin.com/in/mortennielsencom", "https://www.linkedin.com/in/ren%C3%A9-ingemann-pedersen-371b56a", "https://www.linkedin.com/in/charlotte-dyring-phd-175478", "https://www.linkedin.com/in/morten-h%C3%B8strup-s%C3%B8nderholm-9429271a", "https://www.linkedin.com/in/hugo-andersen-6a5152131", "https://www.linkedin.com/in/flemming-rasmussen-9abb66", "https://www.linkedin.com/in/patricklund", "https://www.linkedin.com/in/anders-thyme-rasmussen-6010b237", "https://www.linkedin.com/in/permerfeldt", "https://www.linkedin.com/in/mette-fodgaard-frandsen-4a75a5b0", "https://www.linkedin.com/in/ib-rasmussen-42b24746", "https://www.linkedin.com/in/mikaelejrnaes", "https://www.linkedin.com/in/henrik-pedersen-3135a72", "https://www.linkedin.com/in/preben-mehlsen-42ba99139", "https://www.linkedin.com/in/lasse-bjerning-7416ba31", "https://www.linkedin.com/in/jens-hedegaard-33694925", "https://www.linkedin.com/in/thomas-kanstrup-christensen-5407322", "https://www.linkedin.com/in/pia-bru-petersen-3558583", "https://www.linkedin.com/in/morten-bagger-40b9b887", "https://www.linkedin.com/in/michael-ariel-nielsen-27540a18?authType=name&authToken=KpbG&trk=contacts-contacts-list-contact_name-0", "https://www.linkedin.com/in/kristianharley", "https://www.linkedin.com/in/knut-akselvoll-b4457223", "https://www.linkedin.com/in/erik-tronborg-andersen-44625711", "https://www.linkedin.com/in/pernille-hjort-5098923", "https://www.linkedin.com/in/birgerolsen", "https://www.linkedin.com/in/john-riis-mortensen-4156351", "https://www.linkedin.com/in/mikaelchristensen", "https://www.linkedin.com/in/rene-thomsen", "https://www.linkedin.com/in/mogenscthomsen", "https://www.linkedin.com/in/per-enggrob-larsen-ab6119", "https://www.linkedin.com/in/mikael-nadelmann-17776b", "https://www.linkedin.com/in/anders-drejer-221214", "https://www.linkedin.com/in/jakob-blok-grabow-39ab2b1", "https://www.linkedin.com/in/kim-s%C3%B8g%C3%A5rd-kristensen-b710492", "https://www.linkedin.com/in/preben-nielsen-727a48112", "https://www.linkedin.com/in/sunealstrup", "https://www.linkedin.com/in/kristianholte", "https://www.linkedin.com/in/per-spr%C3%B8gel-68b1581", "https://www.linkedin.com/in/j%C3%B8rgen-thuesen-5b75a510", "https://www.linkedin.com/in/erik-aulk%C3%A6r-andersen-a738313", "https://www.linkedin.com/in/pernille-kallehave-larsen-111876", "https://www.linkedin.com/in/jespergrooss", "https://www.linkedin.com/in/piya-mukherjee-108184bb", "https://www.linkedin.com/in/jorrit-jeroen-water-06451862", "https://www.linkedin.com/in/frank-jensen-91a3378", "https://www.linkedin.com/in/rune-poulsen-2260485a"]


email = input("Email: ").strip()
password = getpass.getpass("Password [Not shown]: ")

scraper = LinkedIn(email=email,
                   password=password)

print("Starting scraping")

# Get users
scraper.get_user_info_by_list(url_list)