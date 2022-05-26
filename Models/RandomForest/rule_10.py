def findDecision(obj):
   # Feature: RSI, Instances: 115, Entropy: 0.9934
   if obj[1] == 'Hold':
      # Feature: BB, Instances: 91, Entropy: 0.9612
      if obj[3] == 'Sell':
         # Feature: MACD, Instances: 68, Entropy: 0.9488
         if obj[2] == 'Sell':
            # Feature: SMA1, Instances: 45, Entropy: 0.9825
            if obj[4] == 'Buy':
               # Feature: Closing, Instances: 32, Entropy: 0.896
               if obj[0]<=73.32:
                  # Feature: SMA2, Instances: 28, Entropy: 0.8631
                  if obj[5] == 'Buy':
                     return 'No'
                  elif obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[0]>73.32:
                  # Feature: SMA2, Instances: 4, Entropy: 1.0
                  if obj[5] == 'Sell':
                     return 'No'
                  elif obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'No'
            elif obj[4] == 'Sell':
               # Feature: SMA2, Instances: 13, Entropy: 0.8905
               if obj[5] == 'Buy':
                  # Feature: Closing, Instances: 7, Entropy: 0.9852
                  if obj[0]<=73.32:
                     return 'Yes'
                  elif obj[0]>73.32:
                     return 'No'
                  else:
                     return 'No'
               elif obj[5] == 'Sell':
                  # Feature: Closing, Instances: 6, Entropy: 0.65
                  if obj[0]<=73.32:
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         elif obj[2] == 'Buy':
            # Feature: Closing, Instances: 23, Entropy: 0.8281
            if obj[0]<=73.32:
               # Feature: SMA2, Instances: 18, Entropy: 0.7642
               if obj[5] == 'Sell':
                  # Feature: SMA1, Instances: 16, Entropy: 0.6962
                  if obj[4] == 'Sell':
                     return 'No'
                  elif obj[4] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[5] == 'Buy':
                  # Feature: SMA1, Instances: 2, Entropy: 1.0
                  if obj[4] == 'Sell':
                     return 'No'
                  elif obj[4] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'No'
            elif obj[0]>73.32:
               # Feature: SMA1, Instances: 5, Entropy: 0.971
               if obj[4] == 'Sell':
                  # Feature: SMA2, Instances: 3, Entropy: 0.9183
                  if obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Buy':
                  # Feature: SMA2, Instances: 2, Entropy: 1.0
                  if obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         else:
            return 'No'
      elif obj[3] == 'Hold':
         # Feature: Closing, Instances: 19, Entropy: 0.998
         if obj[0]<=73.32:
            # Feature: MACD, Instances: 16, Entropy: 0.9887
            if obj[2] == 'Buy':
               # Feature: SMA2, Instances: 15, Entropy: 0.9968
               if obj[5] == 'Buy':
                  # Feature: SMA1, Instances: 14, Entropy: 1.0
                  if obj[4] == 'Buy':
                     return 'No'
                  elif obj[4] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[5] == 'Sell':
                  return 'No'
               else:
                  return 'No'
            elif obj[2] == 'Sell':
               return 'No'
            else:
               return 'No'
         elif obj[0]>73.32:
            return 'Yes'
         else:
            return 'Yes'
      elif obj[3] == 'Buy':
         return 'No'
      else:
         return 'No'
   elif obj[1] == 'Sell':
      # Feature: SMA1, Instances: 18, Entropy: 0.3095
      if obj[4] == 'Buy':
         return 'Yes'
      elif obj[4] == 'Sell':
         # Feature: Closing, Instances: 3, Entropy: 0.9183
         if obj[0]<=73.32:
            # Feature: MACD, Instances: 3, Entropy: 0.9183
            if obj[2] == 'Buy':
               # Feature: BB, Instances: 3, Entropy: 0.9183
               if obj[3] == 'Hold':
                  # Feature: SMA2, Instances: 3, Entropy: 0.9183
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         else:
            return 'Yes'
      else:
         return 'Yes'
   elif obj[1] == 'Buy':
      return 'No'
   else:
      return 'No'
