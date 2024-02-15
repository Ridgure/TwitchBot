#!/usr/bin/env python
# -*- coding: utf-8 -*-
# bot.py
elfNamesFemale = ["Aelene", "Aelinor", "Aemma", "Akash", "Alaesa", "Alaglossa", "Alais", "Alauthshae", "Alavara",
                  "Alea", "Alerathla", "Allannia", "Alloralla", "Alys", "Amaryll", "Aquilaen", "Aredhel", "Arwen",
                  "Axilia", "Ayaeqlarune", "Azariah", "Baelen", "Beala", "Bhuraelea", "Blythswana", "Bonnalurie",
                  "Braerindra", "Caerthynna", "Calarel", "Cauladra", "Celebrían", "Chandrelle", "Chasianna",
                  "Chichlandra", "Chin’nesstre", "Chomylla", "Ciyradyl", "Daealla", "Daena", "Daenestra", "Daenys",
                  "Daeondra", "Doreah", "Elaria", "Elenwe", "Ellania", "Elora", "Elwing", "Elyss", "Fhaertala",
                  "Filaurel", "Filauria", "Fildaerae", "Finduilas", "Fraeya", "Gaelira", "Gaerradh", "Galadriel",
                  "Gaylia", "Ghilanna", "Gilgalad", "Glorfindel", "Glynnii", "Gnima", "Gweyr", "Gwynnestri", "Gylledha",
                  "Haalija", "Hacathra", "Haela", "Halaema", "Halaena", "Halama", "Halanaestra", "Hameada", "Holcene",
                  "Holone", "Hycis", "Iahalae", "Ialantha", "Idril", "Ikeshia", "Ilmadia", "Ilyrana", "Ilythyrra",
                  "Imdalac", "Imizael", "Irithiel", "Ithirae", "Iziuel", "Jahandra", "Kaeda", "Kaylessa", "Keara",
                  "Keerla", "Keishara", "Kethryllia", "Keya", "Kyrrha", "Kythaela", "Laamtora", "Laeanna", "Laena",
                  "Laerdya", "Lazziar", "Leandra", "Leilatha", "Liluth", "Llamryl", "Lorelei", "Lúthien", "Lyraesel",
                  "Maaleshiira", "Maegelle", "Maelyrra", "Maeralya", "Mariah", "Meara", "Mereena", "Merlara", "Miriel",
                  "Morwen", "Mylaela", "Myrynda", "Nuovis", "Nushala", "Nylaathria", "Ochyllyss", "Oluevaera", "Phaerl",
                  "Phantyni", "Phelorna", "Phuingara", "Phyrra", "Quaela", "Quamara", "Raejiisa", "Raerauntha",
                  "Rathiain", "Reinys", "Renestrae", "Rubrae", "Ryllae", "Saelihn", "Saélihn", "Saeya", "Sasha",
                  "Shalana", "Shalantha", "Shalheira", "Shandalar", "Shanyrria", "Sharaera", "Sheedra", "Shiera",
                  "Shyael", "Shyllisyrr", "Sinnafain", "Soliania", "Soora", "Sorsasta", "Susklahava", "Sylmae",
                  "Symrustar", "Syndra", "Synnorha", "Syrenese", "Syrune", "Syviis", "Taena", "Taenya", "Taeriel",
                  "Takari", "Talaedra", "Talanashta", "Talila", "Talilia", "Talindra", "Tamara", "Tarasynora",
                  "Teharissa", "Tiatha", "Tsarra", "Tyria", "Urmicca", "Vaella", "Valindra", "Veara", "Vestele",
                  "Viansola", "Violen", "Viserra", "Yaereene", "Yalanilue", "Yathlanae", "Ynshael", "Yrlissa", "Yrneha",
                  "Yrniela", "Zeale", "Zhuirentel"]
elfNameMale = ["Aego", "Aelrindel", "Aerendyl", "Aeson", "Afamrail", "Agis", "Ailmar", "Aithlin", "Akkar", "Alabyran",
               "Aranel", "Arazorwyn", "Beleg", "Beluar", "Biafyndar", "Bialaer", "Braern", "Briareth", "Cameron",
               "Celeborn", "Celebrimbor", "Chathanglas", "Cheyrth", "Círdan", "Cluhurach", "Cluym", "Cohnal", "Conall",
               "Connak", "Cornaith", "Corym", "Curunir", "Cymbiir", "Cystenn", "Daeharice", "Daemeon", "Dakath",
               "Dalyor", "Darcassan", "Dior", "Earendil", "Edrahil", "Eladithas", "Elanjar", "Elaran", "Elashor",
               "Elbauthin", "Elbereth", "Eldaernth", "Eldar", "Eldrin", "Elenaril", "Elenshaer", "Elrond", "Eluchil",
               "Elwin", "Erlan", "Erlathan", "Eroan", "Erolith", "Eschallus", "Estelar", "Etchelion", "Ethlando",
               "Ettrian", "Evindal", "Eyrynnhv", "Eyrynnhv", "Faelar", "Faelyn", "Faeranduil", "Falael", "Feanor",
               "Fenris", "Filvendor", "Fingolfin", "Finrod", "Folduin", "Gael", "Gaemon", "Gil-galad", "Glynkas",
               "Haemir", "Hagduin", "Haladavar", "Halafarin", "Haryk", "Hastos", "Hatharal", "Herbalar", "Horith",
               "Hubyr", "Iarmenor", "Iefyr", "Ievos", "Ilbryn", "Iliven", "Ilthuryn", "Inarie", "Inchel", "Inialos",
               "Injros", "Intevar", "Iolas", "Jassin", "Jhaan", "Jhaartael", "Jhaeros", "Kelkalyn", "Kevan", "Klaern",
                "Kolvar", "Kuornos", "Kuskyn", "Kymil", "Kyrenic", "Kyrtaar", "lrune", "Maiele", "Mithrandir",
               "Molonym", "Molostroi", "Montagor", "Morgan", "Morthil", "Myrddin", "Myriil", "Myrin", "Mythanthar",
               "Naertho", "Naeryndam", "Napraeleon", "Narbeth", "Nardual", "Nelaeryn", "Neldor", "Nerilamin",
               "Nesterin", "Nevarth", "Nhamashal", "Nieven", "Nindr", "Nym", "Onas", "Oribel", "Oritris", "Orndacil",
               "Ornthalas", "Orris", "Orym", "Oslarelar", "Otaehryn", "Othorion", "Paeral", "Paeris", "Phaendar",
               "Pharom", "Phraan", "Pirphal", "Pleufan", "Purtham", "Pyrder", "Quaeth", "Raegel", "Raunaeril",
               "Ravaphine", "Reysalor", "Rhistel", "Saelethil", "Saevel", "Seiveril", "Sharian", "Siirist", "Silvyr",
               "Sudryl", "Taenaran", "Taerntym", "Tamnaeuth", "Tannivh", "Tassarion", "Tehlmar", "Therona", "Thingol",
               "Thranduil", "Toross", "Travaran", "Triandal", "Turgon", "Usunaar", "Uthorim", "Vaalyun", "Vaegon",
               "Vaeril", "Venrie", "Virjeon", "Yhendorn", "Ylyndar", "Zabbas", "Zaltarish"]
elfNameAndrogynous = ["Alva", "Aubrey", "Avery", "Cindertine", "Elowen", "Aelinor", "Akash", "Alais", "Baelen",
                      "Elwing", "Gaerradh", "Keya", "Nuovis", "Aithlin", "Círdan", "Corym", "Dior", "Elaran", "Erolith",
                      "Ievos", "Inarie", "Kelkalyn", "Maiele", "Morgan", "Myrin", "Sharian", "Therona"]
elfLastNames = ["Adanell", "Aelasar", "Aelorothi", "Aendryr", "Aerasumé", "Aeravansel", "Aldaval", "Aloiene",
                "Alqualonde", "Amaratharr", "Amarthen", "Ammath", "Amrallatha", "Anuaer", "Ardorius", "Artordhron",
                "Augalvaryl", "Beinion", "Beor", "Braegen", "Briarbosk", "Brightcloak", "Brightsong", "Brightspear",
                "Brightstar", "Brightwing", "Castien", "Caundur", "Celelaeth", "Cererindur", "Chamaranthe", "Clatharla",
                "Corellon", "Cormyth", "Coudoarluth", "Craulnober", "Crystalis", "Cubrinmyr", "Darkbrood", "Darkcloak",
                "Darkwing", "Deryth", "Dor-lomin", "Dragonrider", "Eaglelord", "Ealoloth", "Ealoviel", "Earcorn",
                "Elaéyadar", "Elassidil", "Elerelwa", "Elian", "Elkenmage", "Ellarian", "Elond", "Erladden", "Erlshade",
                "Eroth", "Eruien", "Erunonidan", "Estelda", "Evanara", "Faefindas", "Faelen", "Faenion", "Faenor",
                "Faerondalan", "Felarathael", "Finwe", "Floralei", "Flyleaf", "Frostfang", "Gaelen", "Galaalta",
                "Goldenleaf", "Gourael", "Greencloak", "Gretsekul", "Gwaelon", "Hadirsyr", "Hador", "Haell", "Haerlgent", "Haleth",
                "Hasterien", "Hatanar", "Helion", "Hessarion", "Idhtulcdrach", "Ievos", "Iliathorr", "Ilnatar",
                "Immeril", "Impanton", "Imphenon", "Ipyllasc", "Irian", "Isiliraiellyn", "Kadhorduil", "Kithsidhion",
                "Kraok", "Laedireil", "Laelithar", "Lannarseer", "Laralytha", "Larbrinlal", "Larenthanil", "Larethian",
                "Lashrael", "Lassagaseer", "Lasslail", "Leaadion", "Liondale", "Lithelon", "Lithron", "Maedhros",
                "Maeglin", "Maeir", "Maertel", "Magor", "Maltathdar", "Moondown", "Moonflower", "Moonford", "Moonglade",
                "Moonshrine", "Moorfly", "Nenaias", "Nhachashaal", "Nhaéslal", "Nharimlur", "Nightstar", "Nightswatch",
                "Nightwing", "Noldorin", "Norodiir", "Northstar", "Oaktree", "Ongluth", "Orama", "Orbryn", "Quendi",
                "Redwing", "Rhothomir", "Rhuidhen", "Rhyllgallohyr", "Rivleam", "Rivvikyn", "Runemaster", "Sarsantyr",
                "Selakiir", "Selmer", "Shinestar", "Shiredove", "Silkstream", "Siltral", "Silverbow", "Silverhand",
                "Silveroak", "Silverspear", "Simserion", "Snowfell", "Snowreign", "Stillhawk", "Stilmyst", "Stormspear",
                "Straeth", "Strongbow", "Suldusk", "Sunfoal", "Sunshield", "Sunstar", "Sylleth", "Tassarion", "Tathdel",
                "Taurntyrith", "Telerie", "Tellynnan", "Teshurr", "Thalien", "Thoimion", "Thothiion", "Thundruil",
                "Tipantdon", "Turnvale", "Tyrell", "Vanamaeduil", "Vanvathar", "Vispasial", "Voronbund", "Vyshaan",
                "Waelvor", "Werloththar", "Whitethistle", "Windslore", "Windstar", "Windwalker", "Wingglide",
                "Wintermoon", "Wolfspeak", "Yrauos"]
batMaleNames = ['Matrix', 'Fuzz', 'Tiberius', 'Impaler', 'Shrike', 'Vulkan', 'Butch', 'Guano', 'Ripmaw', 'Vamp',
                'Nightmare', 'Baxter', 'Azar', 'Lockjaw', 'Booboo', 'Darth', 'Dimitri', 'Blues', 'Moon', 'Shrike',
                'Midnight', 'Sonar', 'Flaps', 'Screech', 'Draculon', 'Sabath', 'Angel', 'Vladimir', 'Grey', 'Spuds',
                'Dexter', 'Mothra', 'Cole', 'Dimitri', 'Archangel', 'Bruce', 'Drake', 'Comet', 'Spectre', 'Rascal',
                'Blade', 'Nyx', 'Basil', 'Char', 'Wingnut', 'Orion', 'Shadow', 'Brutus', 'Ash', 'Lucifer']
batFemaleNames = ['Angel', 'Trixy', 'Ruth', 'Rhyme', 'Rhyme', 'Echo', 'Mirage', 'Flutters', 'Bandetta', 'Giggles',
                  'Sona', 'Dawnstar', 'Nibbles', 'Harmony', 'Equina', 'Siren', 'Mittens', 'Sage', 'Cookie', 'Dawnstar',
                  'Moonlight', 'Shine', 'Haze', 'Lady', 'Scarlett', 'Illumina', 'Ivy', 'Morning', 'Abby', 'Sade',
                  'Aine', 'Shade', 'Velvet', 'Aura', 'Azurys', 'Dot', 'Equinox', 'Twilight', 'Iris', 'Cerulean', 'Star',
                  'Violet', 'Raine', 'Lucy', 'Nugget', 'Indigo', 'Skye', 'Skylar', 'Morticia']
topLevelDomains = ["www.", ".af", ".ax", ".al", ".dz", ".as", ".ad", ".ao", ".ai", ".aq", ".ar", ".am", ".aw", ".ac",
                   ".au", ".at", ".az", ".bs", ".bh", ".bd", ".bb", ".eus", ".by", ".be", ".bz", ".bj", ".bm", ".bt",
                   ".bo", ".bq", ".ba", ".bw", ".bv", ".br", ".io", ".vg", ".bn", ".bg", ".bf", ".mm", ".bi", ".kh",
                   ".cm", ".ca", ".cv", ".cat", ".ky", ".cf", ".td", ".cl", ".cn", ".cx", ".cc", ".co", ".km", ".cd",
                   ".cg", ".ck", ".cr", ".ci", ".hr", ".cu", ".cw", ".cy", ".cz", ".dk", ".dj", ".dm", ".do", ".tl",
                   ".ec", ".eg", ".sv", ".gq", ".er", ".ee", ".et", ".eu", ".fk", ".fo", ".fm", ".fj", ".fi", ".fr",
                   ".gf", ".pf", ".tf", ".ga", ".gal", ".gm", ".ps", ".ge", ".de", ".gh", ".gi", ".gr", ".gl", ".gd",
                   ".gp", ".gu", ".gt", ".gg", ".gn", ".gw", ".gy", ".ht", ".hm", ".hn", ".hk", ".hu", ".is", ".in",
                   ".id", ".ir", ".iq", ".ie", ".im", ".il", ".it", ".jm", ".jp", ".je", ".jo", ".kz", ".ke", ".ki",
                   ".kw", ".kg", ".la", ".lv", ".lb", ".ls", ".lr", ".ly", ".li", ".lt", ".lu", ".mo", ".mk", ".mg",
                   ".mw", ".my", ".mv", ".ml", ".mt", ".mh", ".mq", ".mr", ".mu", ".yt", ".mx", ".md", ".mc", ".mn",
                   ".me", ".ms", ".ma", ".mz", ".mm", ".na", ".nr", ".np", ".nl", ".nc", ".nz", ".ni", ".ne", ".ng",
                   ".nu", ".nf", ".nc.tr", ".kp", ".mp", ".no", ".om", ".pk", ".pw", ".ps", ".pa", ".pg", ".py", ".pe",
                   ".ph", ".pn", ".pl", ".pt", ".pr", ".qa", ".ro", ".ru", ".rw", ".re", ".sh", ".kn", ".lc", ".pm",
                   ".vc", ".ws", ".sm", ".st", ".sa", ".sn", ".rs", ".sc", ".sl", ".sg", ".bq", ".an", ".sx", ".an",
                   ".sk", ".si", ".sb", ".so", ".so", ".za", ".gs", ".kr", ".ss", ".es", ".lk", ".sd", ".sr", ".sj",
                   ".sz", ".se", ".ch", ".sy", ".tw", ".tj", ".tz", ".th", ".tg", ".tk", ".to", ".tt", ".tn", ".tr",
                   ".tm", ".tc", ".tv", ".ug", ".ua", ".ae", ".uk", ".us", ".vi", ".uy", ".uz", ".vu", ".va", ".ve",
                   ".vn", ".wf", ".eh", ".ye", ".zm", ".zw", ".org", ".net", ".int", ".edu", ".gov", ".mil", ".arpa"]
emotes = ["Kappa", "MrDestructoid", "BCWarrior", "DansGame", "SwiftRage", "PJSalt", "Kreygasm", "SSSsss",
          "PunchTrees", "FunRun", "SMOrc", "FrankerZ", "BibleThump", "ResidentSleeper", "4Head",
          "FailFish", "Keepo", "ANELE", "BrokeBack", "EleGiggle", "BabyRage", "panicBasket", "WutFace", "HeyGuys",
          "KappaPride", "CoolCat", "NotLikeThis", "riPepperonis", "duDudu", "bleedPurple", "SeemsGood", "MingLee",
          "KappaRoss", "KappaClaus", "OhMyDog", "OPFrog", "SeriousSloth", "KomodoHype", "VoHiYo", "KappaWealth",
          "cmonBruh", "NomNom", "StinkyCheese", "ChefFrank", "FutureMan", "OpieOP", "DxCat", "GivePLZ", "TakeNRG",
          "Jebaited", "CurseLit", "TriHard", "CoolStoryBob", "ItsBoshyTime", "PartyTime", "TheIlluminati",
          "BlessRNG", "TwitchLit", "CarlSmile", "Squid3", "LUL", "PowerUpR", "PowerUpL"]

# Message severities
# Timeout 1 second
timeout1 = ["https://", "http://", "pogchamp", "stinky", "stank", "smelly"]
# Timeout 10 minutes
timeout10 = ["retard", "penis"]
# Timeout 4 hours
timeout4Hours = ["you look tired"]
# Ban
banReasons = ["nigger", "n1gger", "n1gg3r", "nigg3r", "thank you for the donation", "knee_gurl",
              "going around leavin scars", "who do you think you are", "dixie rekt", "hitler", "dumb jew",
              "has donated", "Wanna become famous?", "(only you can see this)", "StreamDetails", "bigfollows",
              "bigfollows ", "dogehype", "Want to become famous?", "bigfo", "mountviewers", 'dogehype', 'dot com']

disney = ["star wars", "diiiiisney", "diisney", "disney", "disknee", "disnee", "lion king", "frozen", "peter pan", "jungle book", "beauty and the beast", "aladdin", "mulan", "high school musical", "let it go", "disne", "disnae", "d1sney"]

messes = ["thermal paste", "pink bows", "rainbow colored bows", "glitter"]

bedTime = ["Go to bed Bug", "It is bedtime Bug", "Go to bed Bug! How many times do I have to tell you...", "Are you in bed yet Bug?", "Mr. Sandman is coming to get you Bug", "*Sings a lullaby for Bug*", "I think you are feeling sleepy Bug", "How long has it been since your last nap Bug?", "*Hands Bug a pillow*"]

#only specifics
slumberA = ["wet", "3D", "2D", "fitful", "fearful", "carefree", "worryful", "peaceful", "ruly", "sassy", "grueling", "dreamy", "comfortable", "uncomfortable", "comfy", "sleepless", "warm", "cold", "soft", "deep", "brief"]
slumberAn = ["unholy", "imaginary", "undead", "undisturbed", "eternal", "unconscious"]
riseType = ["weirdly", "cowardly", "reluctantly", "shakily"]
getUpType = ["carefully", "energetically", "staggeringly", "haltingly", "clumsily"]

#exclusive
#if you can both slumber and rise or get up with its adverb
exclusiveAdjectiveA = ["slow", "quick", "chaotic", "careful", "weird"]
exclusiveAdjectiveAn = ["uncomfortable", "animalistic"]
#if you can both rise and get up with it
exclusiveAdverb = ["uncomfortably", "animalistically", "crankily", "sheepishly", "slowly", "quickly", "chaotically", "hungrily", "abruptly", "weirdly", "laughingly", "jumpingly", "sweatingly", "instinctively", "instantly"]
